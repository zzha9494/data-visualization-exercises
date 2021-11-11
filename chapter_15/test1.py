from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


def roll_5_dice():
    results = []
    for time in range(5):
        result = Die().roll()
        results.append(result)
    # print(results)
    return results


def count_result(results):
    results_dict = {}
    for number in range(1, 7):
        times = results.count(number)
        results_dict[number] = times
    # print(results_dict)

    for key, value in results_dict.items():
        if key != 1:
            results_dict[key] += results_dict[1]
    for key, value in results_dict.items():
        if value == 5:
            results_dict[key] = 6
    return results_dict


def play(num=3):
    results_ = {}
    for i in range(1, 7):
        results_[i] = 0
    for time in range(num):
        results = count_result(roll_5_dice())
        # print(results.values())
        for key, value in results.items():
            results_[key] += value
    # print(results_.values())
    return results_.values()


people = 3
results = []
for time in range(10000):
    a = play(people)
    results.append(max(a))

x_value = list(range(people, people * 6 + 1))
y_value = []
for number in x_value:
    y_value.append(results.count(number))

data = [Bar(x=x_value, y=y_value)]
x_axis_config = {'title': 'number', 'dtick': 1}
y_axis_config = {'title': 'times'}
my_layout = Layout(title='roll dice', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename=r'C:\Users\ZiJie.Zhao\Desktop\roll_dice.html')
