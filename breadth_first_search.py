from new_state import *


def breadth_first_search(start, goal, m, n):
    # The set of discovered nodes that need to be (re-)expanded.
    # Initially, only the start node is known.
    open_set = { start }  # openSet := {start}
    closed_set = set()

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    father_of = { start: None }  # cameFrom := an empty map

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    g = {}  # gScore := map with default value of Infinity
    g[start] = 0  # gScore[start] := 0

    # For node n, fScore[n] := gScore[n] + h(n).
    f = {}  # fScore := map with default value of Infinity
    f[start] = 0  # fScore[start] := h(start)

    while open_set:  # while openSet is not empty
        current = min(open_set, key=lambda el: f[el])  # current := the node in openSet having the lowest fScore[] value
        if current == goal:  # if current = goal
            return 'PATH FOUND '  # return reconstruct_path(cameFrom, current)

        open_set.remove(current)  # openSet.Remove(current)
        closed_set.add(current)  # closedSet.Add(current)

        print('open = {}, closed = {}'.format(len(open_set), len(closed_set)), end='\r', flush=True)

        for neighbor in neighbors(current, m, n):  # for each neighbor of current
            if neighbor in closed_set:  # if neighbor in closedSet 
                continue
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            try_value = g[current] + 1                                                # tentative_gScore := gScore[current] + d(current, neighbor)
            if neighbor not in g.keys() or try_value < g[neighbor]:                   # if tentative_gScore < gScore[neighbor]
                # This path to neighbor is better than any previous one. Record it!
                father_of[neighbor] = current                                         # cameFrom[neighbor] := current
                g[neighbor] = try_value                                               # gScore[neighbor] := tentative_gScore
                f[neighbor] = g[neighbor]                                             # fScore[neighbor] := gScore[neighbor] + h(neighbor)
                if neighbor not in open_set:                                          # if neighbor not in openSet
                    open_set.add(neighbor)                                            # openSet.add(neighbor)

    return None
  # // Open set is empty but goal was never reached
  # return failure