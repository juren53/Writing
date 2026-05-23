#-----------------------------------------------------------
# tdb.py - touch the latest db with current date and time 
# 
# Tue 03 Jan 2023 07:14:21 AM CST   Created
#
#
#  
#-----------------------------------------------------------
import os
import glob
import datetime
import csv
from pathlib import Path

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, '..'))
_DATA_DIR = os.environ.get('GB_DATA', os.path.join(_PROJECT_DIR, 'Data'))
_CODE_DIR = _SCRIPT_DIR
_REPORTS_DIR = os.path.join(_PROJECT_DIR, 'gb1_analysis')

os.chdir(_DATA_DIR)

# latest = max([f for f in os.listdir('.') if f.lower().endswith('.csv')], key=os.path.getctime)

# the following finds the latest file by date embedded in the filename

os.chdir(_DATA_DIR)

# List the filenames in the current directory
filenames = [f for f in os.listdir('.') if f.startswith('GB-') and f.endswith('.csv')]

# Sort the list of filenames
filenames.sort()

# Print the first filename
latest = (filenames[-1])
print(filenames[-1])

# the following "touches" the file with the current date and time using the pathlib library

Path(latest).touch()




