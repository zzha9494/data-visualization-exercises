import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = r'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get the date, high, low
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'missing data for {date}')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# draw the chart according to high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='b', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='b', alpha=0.1)

# set the format
ax.set_title('the daily temperature of 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('temperature(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
