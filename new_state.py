import numpy as np


class State:

    def __init__(self, np_arr, m, n):
        self.matrix = np.copy(np_arr)
        self.m = m
        self.n = n

    def index_of(self, item):
        return np.where(self.matrix == item)[0][0]

    def __repr__(self):
        return str(self.matrix)

    def __str__(self):
        fmt_str = str(self.matrix.reshape(self.m, self.n))
        return fmt_str.replace('[0', '[_').replace('0', '_')

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __setitem__(self, idx, value):
        self.matrix[idx] = value

    def __eq__(self, item):
        return np.array_equal(self.matrix, item.matrix)

    def __hash__(self):
        return hash(str(self.matrix))


def neighbors(state: State, m, n):

    x, y = state.index_of(0) // n, state.index_of(0) % n
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i, j in offsets:
        if 0 <= x + i < m and 0 <= y + j < n:
            # yield n * (x + i) + (y + j)
            s = State(state.matrix, state.m, state.n)
            s[n * x + y], s[n * (x + i) + (y + j)] = s[n * (x + i) + (y + j)], s[n * x + y]
            yield s


def manhattan_distance(current: State, goal: State, m , n) -> int:

    dist = 0
    for i in range(1, m * n, 1):
        curr_idx = np.where(current.matrix == i)[0][0]
        goal_idx = np.where(goal.matrix == i)[0][0]

        cx, cy = curr_idx // n, curr_idx % n
        gx, gy = goal_idx // n, goal_idx % n

        dist += abs(cx - gx) + abs(cy - gy)

    return dist