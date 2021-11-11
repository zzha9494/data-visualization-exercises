import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_whether_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        head_row = next(reader)
        date_index = head_row.index('DATE')
        high_index = head_row.index('TMAX')
        low_index = head_row.index('TMIN')

        dates, highs, lows = [], [], []
        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                pass
                # print(f'miss {date}')
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)
        return {'date': dates, 'high': highs, 'low': lows}


sitka_data = get_whether_data(r'C:\Users\ZiJie.Zhao\PycharmProjects\data_visualization\chapter_16\data\sitka_weather_2018_simple.csv')
valley_data = get_whether_data(r'C:\Users\ZiJie.Zhao\PycharmProjects\data_visualization\chapter_16\data\death_valley_2018_simple.csv')

plt.style.use('seaborn')
fig, ax = plt.subplots()
# 绘制sitka图
ax.plot(sitka_data['date'], sitka_data['high'], c='r', alpha=0.6)
ax.plot(sitka_data['date'], sitka_data['low'], c='b', alpha=0.6)
plt.fill_between(sitka_data['date'], sitka_data['high'], sitka_data['low'], facecolor=['b'], alpha=0.15)

# 绘制valley图
ax.plot(valley_data['date'], valley_data['high'], c='r', alpha=0.3)
ax.plot(valley_data['date'], valley_data['low'], c='b', alpha=0.3)
plt.fill_between(valley_data['date'], valley_data['high'], valley_data['low'], facecolor=['b'], alpha=0.05)

# 设置格式
ax.set_title('the daily temperature of 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('temperature(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()
