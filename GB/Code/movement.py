#!/usr/bin/python3
# movement.py - ver 0.3
#-----------------------------------------------------------
# a Movement Report program displaying the movement of GB Names 
# by Rank over time,
#  
# Usage: python movement.py [weekly|monthly|60day|90day]
# 
# Wed 18 Sep 2024 17:32:57 AM CDT Created - hard coded date files
# Thu 19 Sep 2024 10:39:46 AM CDT added routine to automatic dates
# Sat 22 Jun 2025 15:05:00 PM CDT added command line options
#
#
#-----------------------------------------------------------

import csv
import operator
import sys

from datetime import datetime, timedelta
import os
import glob

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, '..'))
_DATA_DIR = os.environ.get('GB_DATA', os.path.join(_PROJECT_DIR, 'Data'))
_CODE_DIR = _SCRIPT_DIR
_REPORTS_DIR = os.path.join(_PROJECT_DIR, 'gb1_analysis')

# Parse command line arguments
if len(sys.argv) > 1:
    period = sys.argv[1].lower()
    if period == 'weekly':
        n = 7
        period_name = "Weekly"
    elif period == 'monthly':
        n = 30
        period_name = "Monthly"
    elif period == '60day':
        n = 60
        period_name = "60-Day"
    elif period == '90day':
        n = 90
        period_name = "90-Day"
    else:
        print("Usage: python movement.py [weekly|monthly|60day|90day]")
        print("Default: weekly (7 days back)")
        sys.exit(1)
else:
    # Default to weekly if no argument provided
    n = 7
    period_name = "Weekly"

os.chdir(_DATA_DIR)
      
# pulls latest GB data filename from /home/juren/Projects/GB/Data
latest = max([f for f in os.listdir('.') if f.startswith('GB-') and f.lower().endswith('.csv')], key=os.path.getctime)

# Extract date from latest filename (e.g., GB-2025-06-22-0900.csv -> 2025-06-22)
latest_date_str = latest[3:13]  # Gets YYYY-MM-DD part
input_date = datetime.strptime(latest_date_str, "%Y-%m-%d")

# Convert to previous date based on n, number of days
previous_day = input_date - timedelta(days=n)

# build previous day filename
previous='GB-'+previous_day.strftime("%Y-%m-%d")+'-0000.csv'


current=(latest[0:13]+'-0000.csv')


# Load data from both files
data_18 = {}
with open(current, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        data_18[row[0]] = {'Rank': int(row[1]), 'Points': int(row[2])}

data_17 = {}
with open(previous, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        data_17[row[0]] = {'Rank': int(row[1]), 'Points': int(row[2])}

# Calculate movement
movement_report = []
for name in data_18:
    if name in data_17:
        rank_diff = data_18[name]['Rank'] - data_17[name]['Rank']
        points_earned = data_18[name]['Points'] - data_17[name]['Points']
        if rank_diff > 0:
            movement = f'Down {rank_diff} places'
        elif rank_diff < 0:
            movement = f'Up {abs(rank_diff)} places'
        else:
            movement = 'Steady'
        movement_report.append({
            'Name': name,
            'Rank': data_18[name]['Rank'],
            'Points': data_18[name]['Points'],
            'PreviousPoints': data_17[name]['Points'],
            'PointsEarned': points_earned,
            'Movement': movement
        })

# Sort report by latest Rank
movement_report.sort(key=operator.itemgetter('Rank'))


print("==================================================")
print(f"{period_name} Movement Report")
print(f"Current:  {current}")
print(f"Previous: {previous} ({n} days ago)")
print("==================================================")

# Print report
print("{:<15} {:>5} {:>10} {:>10} {:>10} {:>10}".format(
    "Name", "Rank", "Points", "Previous", "Earned", "Movement"))
for row in movement_report:
    pts_earned = row['PointsEarned']
    pts_earned_str = f"+{pts_earned:,}" if pts_earned >= 0 else f"{pts_earned:,}"
    print("{:<15} {:>5} {:>10,} {:>10,} {:>10} {:<10}".format(
        row['Name'][:14], row['Rank'], row['Points'], row['PreviousPoints'], pts_earned_str, row['Movement']))


print("==================================================")
print(f"Compared {current} vs {previous}")

