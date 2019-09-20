#!/usr/bin/python3

from n_puzzle import NPuzzleInstance
from min_heap import MinHeap
from algorithms import algorithm

import numpy as np
import matplotlib.pyplot as plt

import os
import sys


_max = 5
my_range = list(range(3, _max+1))
print_sol = False
plt.style.use('dark_background')
n_samples = 1
algs = ['ASTAR', 'BFS']


def plot_graphs(times):

    means = { alg: [vals.mean() for vals in times[alg]] for alg in algs }
    

    t = [i+1 for i in range(1, _max)]
    plt.title(r'$N-Puzzle\ Game\ Solving\ Time$')
    plt.xlabel(r'$Mean\ Of\ 5\ Samples\ Of\ Size\ x^2$'.format(n_samples))
    plt.ylabel(r'$Spent\ Time\ (in\ secs)$')

    plt.xticks(range(1, _max+2))


    for (i, j) in zip(t, means['BFS']):
        bbox_props = dict(boxstyle="round,pad=0.3", fc='green')
        plt.annotate(str(j), xy=(i, j), bbox=bbox_props)

    for (i, j) in zip(t, means['ASTAR']):
        bbox_props = dict(boxstyle="round,pad=0.3", fc='red')
        plt.annotate(str(j), xy=(i, j), bbox=bbox_props)

    plt.plot(t, means['BFS'], 'g', label='BFS')
    plt.plot(t, means['ASTAR'], 'r', label='A Star')
    plt.legend()

    plt.savefig('graphic_time.pdf')
    plt.show()

def statistics():

    for i in my_range:

        times = {
            alg: [
                np.zeros(n_samples) for k in my_range
            ]
            for alg in algs
        }

        P = NPuzzleInstance(i)

        for j, alg in enumerate(algs):
            for k in range(n_samples):

                print('{:02d}/{:02d} - {:02d}/{:02d} - {:02d}/{:02d}'
                        .format(k+1, n_samples, j+1, len(algs), i, _max ),
                    end='\r'
                )

                states, moves, time = algorithm(P, alg).get_solution()
                if states:
                    times[alg][i-3][k] = time.total_seconds()

            P.reset()
        
        print('')
    plot_graphs(times)


if __name__ == '__main__':

    try:
        n_rows = int(sys.argv[1])
        n_cols = int(sys.argv[2])
        rand = int(sys.argv[3])

        P = NPuzzleInstance(n_rows, n_cols, rand=rand)
        print(str(P))

        for alg in algs:

            print(30 * '-')
            print('ALGORITHM USED: ' + alg)

            states, moves, time = algorithm(P, alg).get_solution()

            if states:
                print('FOUND SOLUTION IN: ' + str(time))
                print('MOVEMENTS REQUIRED: ' +str(len(moves)))
                print('MOVES: ' + str(moves))

                size = len(str(states[0]).split('\n')[0])

                for i, state in enumerate(states):
                    print(state)
                    print('')
                    if i < len(moves): print(moves[i].center(size, ' '))
                    print('')
            else:
                print('NOT FOUND')

            print('')
            P.reset()

    except:
        print('Usage: {} n_rows n_cols rand_moves'.format(sys.argv[0]))

