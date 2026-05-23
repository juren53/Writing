#!/usr/bin/python3
# gb1rs.py
#-----------------------------------------------------------
# Points earned by "pack" member between two dates
# and spread 
#Sun 10 Nov 2019 05:23:01 PM CST 
#Thu 24 Feb 2022 00:52:00 AM CST    mod Rank 3 digit INT
#Tue 28 Jun 2022 01:08:51 AM CDT    mod pts 10 digit
#  gb1rs.py
#-----------------------------------------------------------
import pandas as pd
import os
#import easygui
import glob
import datetime
import csv

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, '..'))
_DATA_DIR = os.environ.get('GB_DATA', os.path.join(_PROJECT_DIR, 'Data'))
_CODE_DIR = _SCRIPT_DIR
_REPORTS_DIR = os.path.join(_PROJECT_DIR, 'gb1_analysis')

os.chdir(_DATA_DIR)

db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')])

#os.system('clear')
print('=======================================')
print("Today's Point's           ",db1[3:18])
print('=======================================')


os.chdir(_DATA_DIR)


db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')])


print ("gb1rs.py")
#print(db1[3:18])
day = db1[3:13]

day1f = datetime.date(*[int(i) for i in day.split("-")]) 

one_day = datetime.timedelta(days=1)

day2f= day1f-one_day

db2="GB-"+str(day1f)+'-0000.csv'


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

# The following routine builds a short list of names from the most the list
# using jimbeaux53 as the mid-point in the range of names
# print list.index('jimbeaux53')

slist = []
row = list.index('jimbeaux53') - 9
end = list.index('jimbeaux53') + 8

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
    pts2 = df2.loc[name,'Points']

    rank = df1.loc[name,'Rank']

    print("{:<15}".format(name[:14]),\
        "{0:>5}".format(int(rank)),\
      # "{:<4}".format(str(rank)[:4]),\
        "{0:>7,}".format(pts1-pts2),\
        "{0:>10,}".format(pts1),\
      # "{0:>4,}".format(pts1),\
        "{0:>7,}".format(pts1-jaupts1))

    

    #print "{:<17}".format(name)," ",'\t',\
    #str(rank)[0:4],\
    #"{0:>7,}".format(pts1-pts2),\
    #"{0:>4,}".format(pts1),\
    #"{0:>7,}".format(pts1-jaupts1)








