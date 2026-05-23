#!/usr/bin/python3
# 
#--------------------------------------------
# Points earned by "pack" member for last 60 days
#  gb-60-day.py 
#  updated Sat 16 Nov 2024 18:47:59 AM CST set start time to 0000
#  updated Fri 04 Sep 2025 07:56:34 AM CST added KeyError handling for missing historical users
#-----------------------------------------------------------
import pandas as pd
import os
import glob
import datetime
import csv

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, '..'))
_DATA_DIR = os.environ.get('GB_DATA', os.path.join(_PROJECT_DIR, 'Data'))
_CODE_DIR = _SCRIPT_DIR
_REPORTS_DIR = os.path.join(_PROJECT_DIR, 'gb1_analysis')

 
#os.system('clear')
print('=======================================')
print('60 Day        [gb-60-day.py 2024-11-16]')
print('=======================================')


os.chdir(_DATA_DIR)

        
latest = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

day = latest[3:13]

db1 = "GB-"+day+"-0000.csv"

print("60 days from "+db1[3:18])


day1f = datetime.date(*[int(i) for i in day.split("-")]) 

one_day = datetime.timedelta(days=1)

day2f= day1f-(one_day*60)


db2="GB-"+str(day2f)+'-'+db1[14:18]+'.csv'

# The following routine builds a list of names from the most recent GB*.csv file
with open(db1, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        list = []
        r = 0
        for row in reader:
                r = r+1
                Rank = row[1]
                Name = row[0]
                list.append(Name)

# The following routine builds a short list of names from the list names
# using jimbeaux53 as the mid-point in the range of names

slist = []
row = list.index('jimbeaux53') - 22
end = list.index('jimbeaux53') + 20

while row < end:
	
	slist.append(list[row])
	row = row + 1

#print slist

#-----  jimbeaux53 baseline --------

df1 = pd.read_csv(db1,index_col='Name')
jaupts1 = df1.loc['jimbeaux53','Points']
df2 = pd.read_csv(db2,index_col='Name')
jaupts2 = df2.loc['jimbeaux53','Points']



for x in slist:

        name = x
        

        df1 = pd.read_csv(db1,index_col='Name')
        pts1 = df1.loc[name,'Points']
        df2 = pd.read_csv(db2,index_col='Name')
        
        # Check if user exists in historical data (60 days ago)
        if name in df2.index:
            pts2 = df2.loc[name,'Points']
        else:
            # New user - assume they started with 0 points 60 days ago
            pts2 = 0

        rank = df1.loc[name,'Rank']

        print("{:<12}".format(name[:12]),\
        "{:<4}".format(str(rank)[:4]),\
        "{0:>7,}".format(pts1-pts2),\
        "{0:>7,}".format(int((pts1-pts2)/60)),\
        "{0:>4,}".format(pts1),\
        "{0:>7,}".format(pts1-jaupts1))







