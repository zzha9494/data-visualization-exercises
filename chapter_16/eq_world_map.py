import plotly.express as px

from eq_explore_data import data

fig = px.scatter(
    data,
    x='longitude',
    y='latitude',
    labels={'x': 'longitude', 'y': 'latitude'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='scatter of eq of the world',
    size='magnitude',
    size_max=10,
    color='magnitude',
    hover_name='location'
)
fig.write_html("global_earthquakes.html")
fig.show()
