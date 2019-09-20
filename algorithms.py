from n_puzzle import NPuzzleInstance
from min_heap import MinHeap
import numpy as np
from state import State
from datetime import datetime as time


def algorithm(P: NPuzzleInstance, name='ASTAR'):

    begin = time.now()
    open_heap = MinHeap()
    open_heap.push(P.initial_state, P.initial_state.get_total_cost() if name == 'ASTAR' else P.initial_state.greedy_value)
    cost_so_far = { P.initial_state: 0 }
    father_of = { P.initial_state: None }

    while not open_heap.is_empty():

        # print('heap size -> ' + str(len(open_heap.elements)), end='\r', flush=True)
        P.current_state = open_heap.pop()

        if P.is_solved():
            P.spent_time = time.now() - begin
            solution = []
            curr = P.current_state
            while curr:
                solution.append(curr)
                curr = father_of[curr]

            P.build_solution(list(reversed(solution)))

            return P

        for neighbor in P.neighbors():
            if neighbor not in cost_so_far.keys() or P.current_state.greedy_value < cost_so_far[neighbor]:
                cost_so_far[neighbor] = P.current_state.greedy_value
                open_heap.push(neighbor, neighbor.get_total_cost() if name == 'ASTAR' else neighbor.greedy_value)
                father_of[neighbor] = State(
                    P.current_state.matrix,
                    P.current_state.greedy_value,
                    P.current_state.heuristic_value if name == 'ASTAR' else 0
                )

    return None