import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()

points_number = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1, c='g')

plt.show()
