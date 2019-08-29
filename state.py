import numpy as np


class State:

    def __init__(self, matrix, greedy_value=0, heuristic_value=0, came_from=None):
        self.matrix = np.copy(matrix)
        self.shape = self.matrix.shape
        self.greedy_value = greedy_value
        self.heuristic_value = heuristic_value
        self.came_from = came_from

    def get_total_cost(self):
        return self.greedy_value + self.heuristic_value

    def get_indexes(self, item):
        x, y = np.where(self.matrix == item)
        return x[0], y[0]

    def __getitem__(self, index):
        return self.matrix[index[0], index[1]]

    def __setitem__(self, index, value):
        self.matrix[index[0], index[1]] = value

    def __eq__(self, state):
        return np.array_equal(self.matrix, state.matrix)

    def __lt__(self, state):
        return self.get_total_cost() < state.get_total_cost()

    def __gt__(self, state):
        return self.get_total_cost() > state.get_total_cost()

    def __str__(self):
        return '{}\nf(n) = g(n) + h(n) = {} + {} = {}\n'.format(
                str(self.matrix).replace(' 0', ' _').replace('[0', '[_'),
                str(self.greedy_value),
                str(self.heuristic_value),
                self.get_total_cost()
            )

    def __repr__(self):
        return '\033[33m{}\033[m'.format(
            str(self.matrix.flatten()).replace(' 0', ' _').replace('[0', '[_')
        )


