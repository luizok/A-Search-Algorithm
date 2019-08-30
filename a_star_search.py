from n_puzzle import NPuzzleInstance
from min_heap import MinHeap
import numpy as np
from state import State


def a_star_search(P: NPuzzleInstance, parents=[]):

    open_heap = MinHeap()
    open_heap.push(P.initial_state, P.initial_state.get_total_cost())
    cost_so_far = { P.initial_state: 0 }
    father_of = { P.initial_state: None }

    while not open_heap.is_empty():

        print('\theap size -> ' + str(len(open_heap.elements)), end='\r', flush=True)
        P.current_state = open_heap.pop()

        if P.is_solved():
            solution = []
            curr = P.current_state
            while father_of[curr]:
                solution.append(curr)
                curr = father_of[curr]

            solution.append(curr)

            return list(reversed(solution))

        for neighbor in P.neighbors():
            new_cost = P.current_state.greedy_value

            if neighbor not in cost_so_far.keys() or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                open_heap.push(neighbor, neighbor.get_total_cost())
                father_of[neighbor] = State(
                    P.current_state.matrix,
                    P.current_state.greedy_value,
                    P.current_state.heuristic_value
                )

    return None
