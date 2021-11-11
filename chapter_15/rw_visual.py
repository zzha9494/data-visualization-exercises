import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # create an instance of random walk and calculate
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    points_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=1, c=points_number, cmap=plt.cm.Blues, edgecolors='none')

    # emphasize the start and end point
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # hide the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('continue?')
    if keep_running == 'n':
        break
