from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create a 6 sides die
die = Die()

# roll dice and store the results
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyse the result
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
x_value = list(range(1, die.num_sides + 1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'results'}
y_axis_config = {'title': 'frequencies'}
my_layout = Layout(title='the results of roll 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
