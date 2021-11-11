from random import choice


class RandomWalk:
    """a class to create data of random walk"""

    def __init__(self, num_points=5000):
        """initialize the property"""
        self.num_points = num_points

        # all are start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all points contained in random walk."""
        while len(self.x_values) < self.num_points:

            x_step = self._get_step()
            y_step = self._get_step()

            # refuse to no-walk
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next point
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        """decide the direction and distance"""
        direction = choice([1, -1])
        distance = choice(range(5))
        return direction * distance
