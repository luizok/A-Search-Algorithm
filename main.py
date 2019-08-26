from n_puzzle import NPuzzleInstance
from min_heap import MinHeap
import numpy as np


if __name__ == '__main__':

    instance = NPuzzleInstance(3)
    print(str(instance))
    instance.calculate_distance()

    heap = MinHeap()
    n = 20
    itens = np.random.randint(10, 100, (n, 1))
    priors = np.random.randint(1, 15, (n, 1))

    for item, prior in zip(itens, priors):
        heap.push(item[0], prior[0])

    print(heap)
    print(heap.pop())
    print(heap)


    