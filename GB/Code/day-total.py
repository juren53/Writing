#!/usr/bin/python
#-----------------------------------------------------------
#     day-total.py  "4" reports GB pack users points by day for the last 7 days

#      Finds day totals for a selected user w/ a loop
#      Updated Tue 20 Sep 2016 05:41:46 PM CDT    
#      Updated Sun 12 Nov 2023 10:35:00 AM CST converted to Python3 formats
#-----------------------------------------------------------
import pandas as pd
import os
#import easygui
import glob
import numpy as np
from pandas import DataFrame, Series
import datetime

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, '..'))
_DATA_DIR = os.environ.get('GB_DATA', os.path.join(_PROJECT_DIR, 'Data'))
_CODE_DIR = _SCRIPT_DIR
_REPORTS_DIR = os.path.join(_PROJECT_DIR, 'gb1_analysis')


# os.system('clear')		# clears the screen

print("=======================================")
print("      Day Totals for Last 7 Days ")
print("=======================================")

os.chdir(_DATA_DIR)


pack = []
with open('list.txt', 'r') as f:
    for line in f.readlines():
        l,name = line.strip().split(',')
        pack.append((l,name))

db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)


db1 = db1[0:13]+'-0000.csv'        # Rebuilds most recent filename at midnite

day = db1[3:13]

day1f = datetime.date(*[int(i) for i in day.split("-")]) 

one_day = datetime.timedelta(days=1)

day2f= day1f-one_day
day3f= day1f-(one_day*2)   
day4f= day1f-(one_day*3) 
day5f= day1f-(one_day*4)
day6f= day1f-(one_day*5)
day7f= day1f-(one_day*6)
day8f= day1f-(one_day*7)

db2="GB-"+str(day2f)+'-0000.csv'
db3="GB-"+str(day3f)+'-0000.csv'
db4="GB-"+str(day4f)+'-0000.csv'
db5="GB-"+str(day5f)+'-0000.csv'
db6="GB-"+str(day6f)+'-0000.csv'
db7="GB-"+str(day7f)+'-0000.csv'
db8="GB-"+str(day8f)+'-0000.csv'

#print db1,db2,db3,db4,db5    

print('\t','\t',\
" ",db2[8:13],\
"  ",db3[8:13],\
"  ",db4[8:13],\
"  ",db5[8:13],\
"  ",db6[8:13],\
"  ",db7[8:13],\
"  ",db8[8:13],\
"     Total")
    
for x in pack:

    name = x[1]
     
    #------------------------------------------------

    df = pd.read_csv(db1,index_col='Name')
    pts1 = df.loc[name,'Points']
    
    df = pd.read_csv(db2,index_col='Name')
    #print db2[3:13],
    pts2 = df.loc[name,'Points']

    #print "Points =",pts1-pts2
    p1 = pts1-pts2
    # -------------------------------------------------

    df = pd.read_csv(db2,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db3,index_col='Name')
    #print db3[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p2 = pts1-pts2
    # -------------------------------------------------

    df = pd.read_csv(db3,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db4,index_col='Name')
    #print db4[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p3 = pts1-pts2

    # -------------------------------------------------

    df = pd.read_csv(db4,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db5,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p4 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db5,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db6,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p5 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db6,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db7,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p6 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db7,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db8,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p7 = pts1-pts2
    #-------------------------------------------------


    print("{:<15}".format(name),\
    "{0:>7,}".format(p1),"",\
    "{0:>7,}".format(p2),"",\
    "{0:>7,}".format(p3),"",\
    "{0:>7,}".format(p4),"",\
    "{0:>7,}".format(p5),"",\
    "{0:>7,}".format(p6),"",\
    "{0:>7,}".format(p7),"  ",\
    "{0:>8,}".format(p1+p2+p3+p4+p5+p6+p7))

#"{0:>4,}".format(pts1)



    
