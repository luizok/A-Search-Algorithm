from n_puzzle import NPuzzleInstance
from min_heap import MinHeap
import numpy as np
from a_star_search import a_star_search


if __name__ == '__main__':

    instances = [
        [[1, 8, 2], [0, 4, 3], [7, 6, 5]],  # MUST WORK
        [[13, 2, 10, 3], [1, 12, 8, 4], [5, 0, 9, 6], [15, 14, 11, 7]],  # MUST WORK
        [[6, 13, 7, 10], [8, 9, 11, 0], [15, 2, 12, 5], [14, 3, 1, 4]],  # MUST WORK
        [[3, 9, 1, 15], [14, 11, 4, 6], [13, 0, 10, 12], [2, 7, 8, 5]]  # MUST CRUSH
    ]

    for i, instance in enumerate(instances):
        P = NPuzzleInstance(len(instance), initial_state=instance)
        print(str(P))

        states = a_star_search(P)
        print(30 * '-')
        if states:
            print('FOUND SOLUTION')
            for state in states:
                print(state)
        else:
            print('NOT FOUND')

        print('\n\n')