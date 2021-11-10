from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create a 6 sides die
die_1 = Die()
die_2 = Die()

# roll dice and store the results
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyse the result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
x_value = list(range(2, max_result + 1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'results', 'dtick': 1}
y_axis_config = {'title': 'frequencies'}
my_layout = Layout(title='the results of roll 2 dice 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_2.html')
