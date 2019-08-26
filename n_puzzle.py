import numpy as np


class NPuzzleInstance:

    def __init__(self, m=3, n=None, initial_state=None, goal_state=None):
        self.m = m
        self.n = n if n else m  # if n is None, set n = m
        self.neighbors_indexes = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # If user wanna pass an especific initial_state
        if initial_state:
            self.initial_state = initial_state
        else:
            self.initial_state = self.__build_initial_state()

        # If user wanna pass an especific goal_state
        if goal_state:
            self.goal_state = goal_state
        else:
            self.goal_state = self.__build_goal_state()

        self.current_state = self.initial_state

    def __build_initial_state(self):
        c_state = np.arange(self.m * self. n)
        np.random.shuffle(c_state)
        c_state = np.asarray(c_state).reshape((self.m, self.n))

        return c_state

    def __build_goal_state(self):
        g_state = np.arange(self.m * self.n).reshape((self.m, self.n))
        g_state = np.roll(g_state, -1)
        # The line above shifts the 0 (empty space) to the last position
        # Ex.: np.roll([0, 1, 2, ..., m*n-1], -1) --> [1, 2, ..., m*n-1, 0]
        return g_state

    def calculate_distance(self):

        total_distance = 0
        total_diferents = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.initial_state[i, j] != self.goal_state[i, j]:
                    total_diferents += 1
                    g_i, g_j = np.where(self.goal_state == self.initial_state[i, j])
                    g_i, g_j = g_i[0], g_j[0]

                    dx = max(i, g_i) - min(i, g_i)
                    dy = max(j, g_j) - min(j, g_j)

                    total_distance += dx + dy

        print('Total distance = {}'.format(total_distance))
        print('Total diferents = {}'.format(total_diferents))

    def neighbors(self):
        x, y = np.where(self.current_state == 0)
        x, y = x[0], y[0]

        for (i, j) in self.neighbors_indexes:
            if 0 <= x + i < self.m and 0 <= y + j < self.n:
                    neigh = np.copy(self.current_state)
                    neigh[x + i, y + j], neigh[x, y] = neigh[x, y], neigh[x + i, y + j]

                    yield neigh

    def __str__(self):
        shape_str = str(self.goal_state.shape)
        i_state_str = str(self.initial_state).replace(' 0', ' _').replace('[0', '[_')
        g_state_str = str(self.goal_state).replace(' 0', ' _').replace('[0', '[_')

        fmt_str = 'Dimensions: {}\nCurrent State:\n{}\n\nGoal State:\n{}\n'.format(
            shape_str, i_state_str, g_state_str
        )

        return fmt_str