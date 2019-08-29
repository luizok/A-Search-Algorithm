import heapq


class MinHeap:

    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def pop(self):
        return heapq.heappop(self.elements)[1]

    def remove(self, item):
        remove = None
        for i, obj in enumerate(self.elements):
            if item == obj[1]:
                removed = self.elements.pop(i)
                break

        heapq.heapify(self.elements)

        return removed

    def get_min(self):
        return self.elements[0]

    def __rec_print_heap(self, idx, depth, fmt_str=''):
        if idx < len(self.elements):
            fmt_str += '{}{}\n'.format(depth * '\t', self.elements[idx])
            fmt_str += self.__rec_print_heap(2 * idx + 1, depth + 1)
            fmt_str += self.__rec_print_heap(2 * idx + 2, depth + 1)

        return fmt_str

    def __str__(self):
        fmt_str = self.__rec_print_heap(0, 0)
        return fmt_str

    def __iter__(self):
        self.curr_idx = 0
        return self

    def __next__(self):
        if self.curr_idx < len(self.elements):
            self.curr_idx += 1
            return self.elements[self.curr_idx-1]

        raise StopIteration
