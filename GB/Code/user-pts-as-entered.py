#!/usr/bin/python3
#------------ user-pts-as-entered.py []forked from user-pts.py--ver 0.05a ]------------------------
#      Finds hourly points for a selected user w/ a loop
#             Updated Mon 11 Nov 2019 07:46:23 AM CST   
# Created  Tue 19 Mar 2024 07:22:24 AM CDT V 0.01  intitial working loop
# Updated  Tue 19 Mar 2024 11:07:24 AM CDT v 0.02  added argparse CLI variiables
# Updated  Tue 19 Mar 2024 07:08:33 PM CDT v 0,03  fix pts hr out of sync
# Updated  Tue 19 Mar 2024 08:06:45 PM CDT v 0.04  added day of week to listing
# Updated  Wed 20 Mar 2024 19:33:45 PM CDT v 0.05  added argparse error trapping [user-pts12b.py]
# Updated  Thu 21 Mar 2024 01:47:22 AM CDT v 0.05a  added argparse error trapping [user-pts12c.py]
# Updated  Tue 09 Apr 2024 09:20:44 PM CDT  modified print routine to print date time and pts on one line 
#
# TODOs - pts hour out of sync
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
parser = argparse.ArgumentParser(description="Reports hourly points for a selected user. Must enter the users name and number of hours to process.")

# Add the arguments
#parser.add_argument('-v', '--version', action='version', version=get_version)
parser.add_argument('-v', '--version', action='version', version='user-pts.py Ver 0.05d 2024-03--21-0930')
#parser.add_argument('--name', type=str, help='The name of the user')
parser.add_argument('--hrs', type=int, help='Number of hours')
parser.add_argument('--name', type=str, help='The name of the user')

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

num_mos = args.hrs
name = args.name
#num_mos = args.hrs


d = 1


os.chdir(_DATA_DIR)

# Get most recent CSV data file
db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

# Build date [ day ] from most recent file
day = db1[3:16]

# set name for "zero hour"
#hour1f = datetime.datetime(*[int(i) for i in day.split("-")]) 

#set one hour datetime calculations
one_hour = datetime.timedelta(hours=1)

print("==========")
print(name+" v .05e")
print("==========")

i = 0

# set name for "zero hour"
hour1f = datetime.datetime(*[int(i) for i in day.split("-")]) 

# Get most recent CSV data file
db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

hour2f= hour1f-(one_hour)

db2="GB-"+str(hour2f)[0:10]+"-"+str(hour2f)[11:13]+'00.csv'

while i < num_mos:

    df1 = pd.read_csv(db1,index_col='Name')
    pts1 = df1.loc[name,'Points']
    
    df2 = pd.read_csv(db2,index_col='Name')
    pts2 = df2.loc[name,'Points']

    p1 = pts1-pts2

    ######## Day of the week computatiion ##########

    from datetime import datetime, timedelta    
    
    date = db1[3:18]

    date_format = '%Y-%m-%d-%H%M'

    dt = datetime.strptime(date, date_format)

    day_of_week = dt.strftime('%a')
  
    ########### Print routines  ######################
    '''
    # prints zero point hours   - zero points printed
 
    print(db1[3:18]+" "+day_of_week),
    print("                     ",p1)


    # prints ONLY points earned by hour - no zero pts hrs
    '''   
    if p1 != 0:     # tests and avoids zero point hours

        print(db1[3:18]+" "+day_of_week+"    "+str(p1)),
        #print("                     ",p1)

    ##################################################

    db1 = db2

    hour2f= hour2f-(one_hour*d)     

    db2="GB-"+str(hour2f)[0:10]+"-"+str(hour2f)[11:13]+'00.csv'

    i += 1

