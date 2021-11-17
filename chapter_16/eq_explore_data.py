import json

import pandas as pd

# explore the data structure
filename = r'data\eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = r'data\readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_data = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['longitude', 'latitude', 'location', 'magnitude']
)
