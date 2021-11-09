import matplotlib.pyplot as plt

x_value = range(1, 5001)
y_value = [i**3 for i in x_value]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, s=1, c=y_value, cmap=plt.cm.prism)

ax.set_title('lifang', fontsize=24)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)

ax.tick_params(axis='both', labelsize=14, which='major')

plt.show()

