import csv

import matplotlib.pyplot as plt

filename = r'data\sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get the max temperature
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# draw the chart according to high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# set the format
ax.set_title('the high daily temperature of July, 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('temperature(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
