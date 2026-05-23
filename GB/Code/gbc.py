#!/usr/bin/python3
#-----------------------------------------------------------
#
#  Checks for GB members who have earned one month 6K challenge 
#
#  gbchk6k.py   
#  Last updated: 2019-09-08  1415  CDT
#-----------------------------------------------------------
import pandas as pd
import os
import glob
import numpy as np
from pandas import DataFrame, Series
import datetime
import csv

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, '..'))
_DATA_DIR = os.environ.get('GB_DATA', os.path.join(_PROJECT_DIR, 'Data'))
_CODE_DIR = _SCRIPT_DIR
_REPORTS_DIR = os.path.join(_PROJECT_DIR, 'gb1_analysis')

os.system('clear')        # clears the screen
os.chdir(_DATA_DIR)

# gets file name of most recent GB download
db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

# creates a filename for first day of the current month at midnite
db1st = str(db1)[0:11]+'01-0000.csv'

#Compute number of days since 1st of month
beg = int(db1st[11:13])
end = int(db1[11:13])
d=end-beg+1         # d [days from 1st of month used in 


# The following routine builds a list of names from db1 [first of month ]GB*.csv file
with open(db1, 'rt') as csvfile:                          # ~2000 entries in db1
        reader = csv.reader(csvfile, delimiter=',')
        list = []
        r = 0
        for row in reader:
                r = r+1
                Rank = row[1]
                Name = row[0]
                list.append(Name)

# The following routine builds a short list of names from the most the list of names
# using jimbeaux53 as the mid-point in the range of names
# print list.index('jimbeaux53')

slist = []
row = list.index('jimbeaux53') - 9
end = list.index('jimbeaux53') + 8

while row < end:
    
    slist.append(list[row])
    row = row + 1

###################################    

day = db1st[3:13]                    # first day of month in '2020-09-01' format

one_day = datetime.timedelta(days=1) # 'datetime.timedelta(days=1)'

day1f = datetime.date(*[int(i) for i in day.split("-")])

day2f= day1f+one_day                 #  datetime.date(2020, 9, 1)

###################################

print('gbchk6k.py   2020--09-10')
print('--------------------')

#  nested loop - number of days from 1st of month - members in slist
i = 1
while i < d:                        # loops for number of days since 1st of month 

    for x in slist:                 # loops thru entries in slist

        name = x                     # pulls next name from slist

        db1="GB-"+str(day1f)+'-0000.csv'  # sets beginning file
        db2="GB-"+str(day2f)+'-0000.csv'  # sets ending file

        df = pd.read_csv(db1,index_col='Name')  # pulls record for name 
        pts1 = df.loc[name,'Points']            # extracts points from record
    
        df = pd.read_csv(db2,index_col='Name')  # pulls record for name
        pts2 = df.loc[name,'Points']            # extracts points from record

        p1 = pts2-pts1                          #computes mbrs points for the day

        rank = df.loc[name,'Rank']

        if(p1 > 6000):                          #if points exceed 6K print 
                                                #name and points
            print("{:<17}".format(name),"{0:>7,}".format(p1),int(rank), day1f)

    day = day1f + one_day                       #increments day by one
    day1f = day                                 # resets formated beginning ing day 
    day2f= day1f+one_day                        # resets formated ending day

    
    print('    Day ',i,day - one_day)           # print header for day
    print('--------------------')

    i = i + 1
