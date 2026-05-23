# Import the necessary libraries
import sys
import os
import pandas as pd
import datetime
import argparse
from IPython.display import display, HTML
from sys import stdout
import IPython.display as display

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, '..'))
_DATA_DIR = os.environ.get('GB_DATA', os.path.join(_PROJECT_DIR, 'Data'))
_CODE_DIR = _SCRIPT_DIR
_REPORTS_DIR = os.path.join(_PROJECT_DIR, 'gb1_analysis')
#from IPython.core.ui import InternalIPythonError

# Define the paging function
def paged_output(data):
    try:
        if len(data) > 10:
            pager = get_ipython().display_formatter.formatters['text/plain'].pprint
            pager(data, max_lines=10, end_lines=10)
        else:
            print(data)
    except InternalIPythonError:
        print(data)

# Set up the command-line arguments
parser = argparse.ArgumentParser(description="Reports hourly points for a selected user.")
parser.add_argument('-v', '--version', action='version', version='user-pts.py Ver 0.05d 2024-03--21-0930')
parser.add_argument('--hrs', type=int, help='Number of hours')
parser.add_argument('--name', type=str, help='The name of the user')

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

# Set up the variables
num_mos = args.hrs
name = args.name

# Set up the directories and files
os.chdir(_DATA_DIR)

# Get the most recent CSV data file
db1 = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

# Set up the data frames
day = db1[3:16]
one_hour = datetime.timedelta(hours=1)
hour1f = datetime.datetime(*[int(i) for i in day.split("-")])
hour2f = hour1f - one_hour
db2 = "GB-" + str(hour2f)[0:10] + "-" + str(hour2f)[11:13] + '00.csv'

# Set up the paging
stdout.reconfigure(line_buffering=True)
i = 0

# Process the data
while i < num_mos:
    df1 = pd.read_csv(db1, index_col='Name')
    pts1 = df1.loc[name, 'Points']
    df2 = pd.read_csv(db2, index_col='Name')
    pts2 = df2.loc[name, 'Points']
    p1 = pts1 - pts2
    from datetime import datetime, timedelta
    date = db1[3:18]
    date_format = '%Y-%m-%d-%H%M'
    dt = datetime.strptime(date, date_format)
    day_of_week = dt.strftime('%a')
    # Print the data
    print(db1[3:18] + " " + day_of_week)
    print("                     ", p1)
    # Move to the next data file
    db1 = db2
    hour2f = hour2f - one_hour
    db2 = "GB-" + str(hour2f)[0:10] + "-" + str(hour2f)[11:13] + '00.csv'
    i += 1

# Clean up
del sys
