class Fringe:
    def __init__(self, sort_func=lambda x: x):
        self._queue = []
        self._sort_func = sort_func

    def __containes__(self, element):
        return element in self._queue
    
    def __iter__(self):
        return iter(self._queue)

    def _sort(self):
        self._queue.sort(key=self._sort_func)

    def enqueue(self,node):
        self._queue.append(node)
        self._sort()

    def dequeue(self):
        return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0
    
    def remove(self, element):
        if element in self._queue:
            self._queue.remove(element)