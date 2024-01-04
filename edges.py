class BlockedEdge:
    def __init__(self, x1, y1, x2, y2):
        self.x1y1 = tuple([x1, y1])
        self.x2y2 = tuple([x2, y2])


class FragileEdge:
    def __init__(self, x1, y1, x2, y2):
        self.x1y1 = tuple([x1, y1])
        self.x2y2 = tuple([x2, y2])
        self.visited = False
