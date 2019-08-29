from n_puzzle import NPuzzleInstance
from min_heap import MinHeap
import numpy as np


def a_star_search(P: NPuzzleInstance, parents=[]):
#   OPEN = priority queue containing START
#   CLOSED = empty set
#   while lowest rank in OPEN is not the GOAL:
#     current = remove lowest rank item from OPEN
#     add current to CLOSED
#     for neighbors of current:
#       cost = g(current) + movementcost(current, neighbor)
#       if neighbor in OPEN and cost less than g(neighbor):
#         remove neighbor from OPEN, because new path is better
#       if neighbor in CLOSED and cost less than g(neighbor): ⁽²⁾
#         remove neighbor from CLOSED
#       if neighbor not in OPEN and neighbor not in CLOSED:
#         set g(neighbor) to cost
#         add neighbor to OPEN
#         set priority queue rank to g(neighbor) + h(neighbor)
#         set neighbor's parent to current
#   reconstruct reverse path from goal to start
#   by following parent pointers
    return