import csv

import pandas as pd
import plotly.express as px

filename = 'world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lon_index = header_row.index('longitude')
    lat_index = header_row.index('latitude')
    bri_index = header_row.index('brightness')

    lons, lats, bris = [], [], []
    for row in reader:
        lons.append(float(row[lon_index]))
        lats.append(float(row[lat_index]))
        bris.append(float(row[bri_index]))

data = pd.DataFrame(
    data=zip(lons, lats, bris), columns=['longitude', 'latitude', 'brightness']
)

fig = px.scatter(
    data,
    x='longitude',
    y='latitude',
    labels={'x': 'longitude', 'y': 'latitude'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title=str(filename[:-4]),
    size='brightness',
    size_max=10,
    color='brightness',
)
fig.write_html(str(filename[:-4]) + '.html')
fig.show()
