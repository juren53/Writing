#!/usr/bin/python
#-----------------------------------------------------------
#      Finds day totals for a short range of users 
#             Updated Mon 11 Nov 2019 07:46:23 AM CST   
#   gb2rs.py        Users points by hour for the range
#  updated on Sun 20 Aug 2023 12:13:07 AM CDT  extended to 25 hr time frame
#  update on Thu 29 Aug 2024 06:02:35 PM CDT  added rank column
#-----------------------------------------------------------
import pandas as pd
import os
#import easygui
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


#os.system('clear')        # clears the screen

print("=======================================")
print("          By Hour Point Totals         ")
print("=======================================")

os.chdir(_DATA_DIR)

    
db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

#db1 = db1[0:13]+'-0000.csv'        # Rebuilds most recent filename at midnite

day = db1[3:16]
print("gb2rs.py","                                           ",db1[3:18])

hour1f = datetime.datetime(*[int(i) for i in day.split("-")]) 

one_hour = datetime.timedelta(hours=1)


hour2f= hour1f-one_hour
hour3f= hour1f-(one_hour*2) 
hour4f= hour1f-(one_hour*3) 
hour5f= hour1f-(one_hour*4) 
hour6f= hour1f-(one_hour*5) 
hour7f= hour1f-(one_hour*6) 
hour8f= hour1f-(one_hour*7) 
hour9f= hour1f-(one_hour*8) 
hour10f= hour1f-(one_hour*9) 
hour11f= hour1f-(one_hour*10) 
hour12f= hour1f-(one_hour*11) 
hour13f= hour1f-(one_hour*12) 
hour14f= hour1f-(one_hour*13) 
hour15f= hour1f-(one_hour*14) 
hour16f= hour1f-(one_hour*15) 
hour17f= hour1f-(one_hour*16) 
hour18f= hour1f-(one_hour*17) 
hour19f= hour1f-(one_hour*18) 
hour20f= hour1f-(one_hour*19) 
hour21f= hour1f-(one_hour*20) 
hour22f= hour1f-(one_hour*21) 
hour23f= hour1f-(one_hour*22) 
hour24f= hour1f-(one_hour*23)
hour25f= hour1f-(one_hour*24)
hour26f= hour1f-(one_hour*25)
hour27f= hour1f-(one_hour*25)


db2="GB-"+str(hour2f)[0:10]+"-"+str(hour2f)[11:13]+'00.csv'
db3="GB-"+str(hour3f)[0:10]+"-"+str(hour3f)[11:13]+'00.csv'
db4="GB-"+str(hour4f)[0:10]+"-"+str(hour4f)[11:13]+'00.csv'
db5="GB-"+str(hour5f)[0:10]+"-"+str(hour5f)[11:13]+'00.csv'
db6="GB-"+str(hour6f)[0:10]+"-"+str(hour6f)[11:13]+'00.csv'
db7="GB-"+str(hour7f)[0:10]+"-"+str(hour7f)[11:13]+'00.csv'
db8="GB-"+str(hour8f)[0:10]+"-"+str(hour8f)[11:13]+'00.csv'
db9="GB-"+str(hour9f)[0:10]+"-"+str(hour9f)[11:13]+'00.csv'
db10="GB-"+str(hour10f)[0:10]+"-"+str(hour10f)[11:13]+'00.csv'
db11="GB-"+str(hour11f)[0:10]+"-"+str(hour11f)[11:13]+'00.csv'
db12="GB-"+str(hour12f)[0:10]+"-"+str(hour12f)[11:13]+'00.csv'
db13="GB-"+str(hour13f)[0:10]+"-"+str(hour13f)[11:13]+'00.csv'
db14="GB-"+str(hour14f)[0:10]+"-"+str(hour14f)[11:13]+'00.csv'
db15="GB-"+str(hour15f)[0:10]+"-"+str(hour15f)[11:13]+'00.csv'
db16="GB-"+str(hour16f)[0:10]+"-"+str(hour16f)[11:13]+'00.csv'
db17="GB-"+str(hour17f)[0:10]+"-"+str(hour17f)[11:13]+'00.csv'
db18="GB-"+str(hour18f)[0:10]+"-"+str(hour18f)[11:13]+'00.csv'
db19="GB-"+str(hour19f)[0:10]+"-"+str(hour19f)[11:13]+'00.csv'
db20="GB-"+str(hour20f)[0:10]+"-"+str(hour20f)[11:13]+'00.csv'
db21="GB-"+str(hour21f)[0:10]+"-"+str(hour21f)[11:13]+'00.csv'
db22="GB-"+str(hour22f)[0:10]+"-"+str(hour22f)[11:13]+'00.csv'
db23="GB-"+str(hour23f)[0:10]+"-"+str(hour23f)[11:13]+'00.csv'
db24="GB-"+str(hour24f)[0:10]+"-"+str(hour24f)[11:13]+'00.csv'
db25="GB-"+str(hour25f)[0:10]+"-"+str(hour25f)[11:13]+'00.csv'
db26="GB-"+str(hour26f)[0:10]+"-"+str(hour26f)[11:13]+'00.csv'
db27="GB-"+str(hour27f)[0:10]+"-"+str(hour27f)[11:13]+'00.csv'


print("                       ","{:<5}".format(db1[14:18]), end=' ')
print("{:<5}".format(db2[14:18]), end=' ')
print("{:<5}".format(db3[14:18]), end=' ')
print("{:<5}".format(db4[14:18]), end=' ')
print("{:<5}".format(db5[14:18]), end=' ')
print("{:<5}".format(db6[14:18]), end=' ')
print("{:<5}".format(db7[14:18]), end=' ')
print("{:<5}".format(db8[14:18]), end=' ')
print("{:<5}".format(db9[14:18]), end=' ')
print("{:<5}".format(db10[14:18]), end=' ')
print("{:<5}".format(db11[14:18]), end=' ')
print("{:<5}".format(db12[14:18]), end=' ')
print("{:<5}".format(db13[14:18]), end=' ')
print("{:<5}".format(db14[14:18]), end=' ')
print("{:<5}".format(db15[14:18]), end=' ')
print("{:<5}".format(db16[14:18]), end=' ')
print("{:<5}".format(db17[14:18]), end=' ')
print("{:<5}".format(db18[14:18]), end=' ')
print("{:<5}".format(db19[14:18]), end=' ')
print("{:<5}".format(db20[14:18]), end=' ')
print("{:<5}".format(db21[14:18]), end=' ')
print("{:<5}".format(db22[14:18]), end=' ')
print("{:<5}".format(db23[14:18]), end=' ')
print("{:<5}".format(db24[14:18]), end=' ')
print("{:<5}".format(db25[14:18]), end=' ')

print("{:<5}".format(db26[14:18]))
    

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


for x in slist:

    name = x       

    #rank = df.loc[name,'Rank']

    #------------------------------------------------

    df = pd.read_csv(db1,index_col='Name')
    pts1 = df.loc[name,'Points']
    
    df = pd.read_csv(db2,index_col='Name')
    #print db2[3:13],
    pts2 = df.loc[name,'Points']

    #print "Points =",pts1-pts2
    p1 = pts1-pts2

    rank = df.loc[name,'Rank']

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

    df = pd.read_csv(db8,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db9,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p8 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db9,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db10,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p9 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db10,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db11,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p10 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db10,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db11,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p10 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db11,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db12,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p11 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db12,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db13,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p12 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db13,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db14,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p13 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db14,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db15,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p14 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db15,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db16,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p15 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db16,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db17,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p16 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db17,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db18,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p17 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db18,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db19,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p18 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db19,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db20,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p19 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db20,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db21,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p20 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db21,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db22,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p21 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db22,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db23,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p22 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db23,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db24,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p23 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db24,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db25,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p24 = pts1-pts2
    #-------------------------------------------------
    
    df = pd.read_csv(db25,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db26,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p25 = pts1-pts2
    #-------------------------------------------------
       
    df = pd.read_csv(db26,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db27,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p26 = pts1-pts2
    #-------------------------------------------------


    print("{:<17}".format(name), end=' ')
    print("{0:>4}".format(rank), end=' ')
    print("{0:>5}".format(p1), end=' ')
    print("{0:>5}".format(p2), end=' ')
    print("{0:>5}".format(p3), end=' ')
    print("{0:>5}".format(p4), end=' ')
    print("{0:>5}".format(p5), end=' ')
    print("{0:>5}".format(p6), end=' ')
    print("{0:>5}".format(p7), end=' ')
    print("{0:>5}".format(p8), end=' ')
    print("{0:>5}".format(p9), end=' ')
    print("{0:>5}".format(p10), end=' ')
    print("{0:>5}".format(p11), end=' ')
    print("{0:>5}".format(p12), end=' ')
    print("{0:>5}".format(p13), end=' ')
    print("{0:>5}".format(p14), end=' ')
    print("{0:>5}".format(p15), end=' ')
    print("{0:>5}".format(p16), end=' ')
    print("{0:>5}".format(p17), end=' ')
    print("{0:>5}".format(p18), end=' ')
    print("{0:>5}".format(p19), end=' ')
    print("{0:>5}".format(p20), end=' ')
    print("{0:>5}".format(p21), end=' ')
    print("{0:>5}".format(p22), end=' ')
    print("{0:>5}".format(p23), end=' ')
    print("{0:>5}".format(p24), end=' ')
    print("{0:>5}".format(p25), end=' ')

    print("{0:>5}".format(p26))
    


    

