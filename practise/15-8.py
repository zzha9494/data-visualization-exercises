from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() * die_2.roll() for time in range(1000000)]

result_range = range(1, die_1.num_sides * die_2.num_sides + 1)
frequencies = [results.count(value) for value in result_range]

x_value = list(result_range)
data = [Bar(x=x_value, y=frequencies)]
x_axis_config = {'title': 'results', 'dtick': 1}
y_axis_config = {'title': 'frequencies'}
my_layout = Layout(title='the results of roll D6 and D10', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename=r'C:\Users\ZiJie.Zhao\Desktop\test.html')
