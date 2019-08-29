from n_puzzle import NPuzzleInstance
from min_heap import MinHeap
import numpy as np
from a_star_search import a_star_search


if __name__ == '__main__':

    instance = NPuzzleInstance(3)
    print(str(instance))

    a_star_search(instance)
    