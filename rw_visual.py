import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # create an instance of random walk and calculate
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=10)

    plt.show()

    keep_running = input('continue?')
    if keep_running == 'n':
        break
