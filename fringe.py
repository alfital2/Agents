class Fringe:
    def __init__(self, sort_func=lambda x: x):
        self._queue = []
        self._sort_func = sort_func

    def _sort(self):
        self._queue.sort(key=self._sort_func)


    def enqueue(self,node):
        self._queue.append(node)
        self._sort()


    def dequeue(self):
        return self._queue.pop(0)