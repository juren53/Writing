#!/usr/bin/python3
#-----------------user-pts-daily.py  v0.05b] ------------------------
#      Finds daily points for a selected user w/ a loop
#             Updated Thu 29 Jan 2026 12:05:06 PM CST  
# Created  Tue 19 Mar 2024 07:22:24 AM CDT V 0.01  intitial working loop
# Updated  Tue 19 Mar 2024 11:07:24 AM CDT v 0.02  added argparse CLI variiables
# Updated  Tue 19 Mar 2024 07:08:33 PM CDT v 0,03  fix pts day out of sync
# Updated  Tue 19 Mar 2024 08:06:45 PM CDT v 0.04  added day of week to listing
# Updated  Wed 20 Mar 2024 19:33:45 PM CDT v 0.05  added argparse error trapping [user-pts12b.py]
# Updated  Thu 21 Mar 2024 01:47:22 AM CDT v 0.05a  added argparse error trapping [user-pts12c.py]
# Updated  Fri 30 Mar 2024 04:52:06 PM CDT  user-pts.py  broken out to as-entered and daily
# Updated  Fri 05 Apr 2024 04:52:06 PM CDT  changed print routine to single line per day
# Updated  Thu 29 Jan 2026 12:05:06 PM CST  added --jau switch to print additional col w JAUs points 
#
# accomodates - python3 x.py --name jcurley --days 400 | awk '$3 > 6000'  finds day 6k bonus is reached
#
# TODOs - pts day out of sync
#-----------------------------------------------------------
import pandas as pd
import os
import glob
import numpy as np
from pandas import DataFrame, Series
import datetime
import csv
import argparse
#from datetime import datetime, timedelta
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, '..'))
_DATA_DIR = os.environ.get('GB_DATA', os.path.join(_PROJECT_DIR, 'Data'))
_CODE_DIR = _SCRIPT_DIR
_REPORTS_DIR = os.path.join(_PROJECT_DIR, 'gb1_analysis')

# Create the parser
parser = argparse.ArgumentParser(description="Reports daily points for a selected user. Must enter the users name and number of days to process.")

# Add the arguments
#parser.add_argument('-v', '--version', action='version', version=get_version)
parser.add_argument('-v', '--version', action='version', version='user-pts-daily.py Ver 0.06 2024-04--05-1930')
parser.add_argument('--name', type=str, help='The name of the user')
parser.add_argument('--days', type=int, help='Number of days')
parser.add_argument('--jau', action='store_true', help='Add jimbeaux53 points column for comparison')

# Parse the arguments
args = parser.parse_args()


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

try:
    args = parser.parse_args()
except Exception:
    parser.error('see help below')
    parser.print_help()
    parser.exit()
except TypeError:
    parser.error('see help below')
    parser.print_help()
    parser.exit()


name = args.name
num_days = args.days
jau = args.jau
jau_name = 'jimbeaux53'

os.chdir(_DATA_DIR)

# Get most recent CSV data file
db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

# Build date [ day ] from most recent file
day = db1[3:16]

# set name for "zero day"
#day1f = datetime.datetime(*[int(i) for i in day.split("-")])

#set one day datetime calculations
one_day = datetime.timedelta(hours=1)

print("==========")
print(name+" v .05d")
print("==========")

i = 0

# set name for "zero day"
day1f = datetime.datetime(*[int(i) for i in day.split("-")])

# Get most recent CSV data file
db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

day2f= day1f-(one_day)

db2="GB-"+str(day2f)[0:10]+"-"+str(day2f)[11:13]+'00.csv'

while i < num_days:

    df1 = pd.read_csv(db1,index_col='Name')
    pts1 = df1.loc[name,'Points']

    df2 = pd.read_csv(db2,index_col='Name')
    pts2 = df2.loc[name,'Points']

    p1 = pts1-pts2

    if jau:
        jau_pts1 = df1.loc[jau_name,'Points']
        jau_pts2 = df2.loc[jau_name,'Points']
        jau_p1 = jau_pts1-jau_pts2

    ###### Day of the week computatiion #####

    from datetime import datetime, timedelta    
    
    date = db1[3:18]

    date_format = '%Y-%m-%d-%H%M'

    dt = datetime.strptime(date, date_format)

    day_of_week = dt.strftime('%a')
  
    #########################################

    if jau:
        print(f"{db1[3:13]} {day_of_week}  {p1:>6}  {jau_p1:>6}")
    else:
        print(f"{db1[3:13]} {day_of_week}  {p1}")
    #print(db1[3:18]),    

    #p1 = pts1-pts2

    #print("                      ",p1)

    db1 = db2

    day2f= day2f-(one_day*24)

    db2="GB-"+str(day2f)[0:10]+"-"+str(day2f)[11:13]+'00.csv'

    i += 1

