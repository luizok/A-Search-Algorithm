import numpy as np


class State:

    def __init__(self, matrix, greedy_value=0, heuristic_value=0, came_from=None):
        '''
        Creates a new instance of State. This class stores the current state of
        some problem, as well as his greedy cost (g(n)) and his heuristic value (h(n))
        * came_from will be used soon :D
        '''
        self.matrix = np.copy(matrix)
        self.shape = self.matrix.shape
        self.greedy_value = greedy_value
        self.heuristic_value = heuristic_value
        self.came_from = came_from

    def get_total_cost(self):
        '''
        Returns the total cost of the State, a.k.a f(n), where f(n) = g(n) + h(n)
        '''
        return self.greedy_value + self.heuristic_value

    def get_indexes(self, item):
        '''
        Returns the indexes (x, y) of item in the element self.matrix
        '''
        x, y = np.where(self.matrix == item)
        return x[0], y[0]

    def get_func_values_as_str(self):
        return 'f(n) = g(n) + h(n) = {} + {} = {}'.format(
            self.greedy_value, self.heuristic_value, self.get_total_cost()
        )

    def __getitem__(self, index):
        return self.matrix[index[0], index[1]]

    def __setitem__(self, index, value):
        self.matrix[index[0], index[1]] = value

    def __eq__(self, state):
        '''
        Defines when two instances of State are equals
        '''
        return np.array_equal(self.matrix, state.matrix)

    def __lt__(self, state):
        '''
        Defines when some State S¹ < State S²
        '''
        return self.get_total_cost() < state.get_total_cost()

    def __gt__(self, state):
        '''
        Defines when some State S¹ > State S²
        '''
        return self.get_total_cost() > state.get_total_cost()

    def __hash__(self):
        return hash(self.__repr__())

    def __str__(self):
        return str(self.matrix).replace(' 0', ' _').replace('[0', '[_')

    def __repr__(self):
        return '\033[33m{}\033[m'.format(
            str(self.matrix.flatten()).replace(' 0', ' _').replace('[0', '[_')
        )


