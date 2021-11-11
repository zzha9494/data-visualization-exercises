from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

d8_1 = Die(8)
d8_2 = Die(8)

results = []
for time in range(100000):
    result = d8_1.roll() + d8_2.roll()
    results.append(result)

frequencies = []
result_range = range(2, d8_1.num_sides + d8_2.num_sides + 1)
for value in result_range:
    frequency = results.count(value)
    frequencies.append(frequency)

x_value = list(result_range)
data = [Bar(x=x_value, y=frequencies)]
x_axis_config = {'title': 'results', 'dtick': 1}
y_axis_config = {'title': 'frequencies'}
my_layout = Layout(title='the results of roll D6 and D10', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename=r'C:\Users\ZiJie.Zhao\Desktop\test.html')
