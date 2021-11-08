import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [i ** 2 for i in x_value]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, s=10, c=[(0, 0.8, 0)])

# set the title of figure and label of axis
ax.set_title('squares', fontsize=24)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('square of value', fontsize=14)

# set the size of tick
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range of value of each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
