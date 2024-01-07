import Coordinate as Co


class Simulator:
    def __init__(self, data):

        self.grid_rows = data["grid_rows"]
        self.grid_columns = data["grid_columns"]
        self.packages = data["packages"]
        self.blocked_edges = data["blocked_edges"]
        self.fragile_edges = data["fragile_edges"]
        self.graph = self._create_grid_graph()
        self.remove_blocked_edges()
        # self.put_packages()
        self.visualize_graph()

    def _create_grid_graph(self):
        graph = {}
        for x in range(self.grid_columns + 1):
            for y in range(self.grid_rows + 1):
                neighbors = []
                if x > 0:
                    neighbors.append((x - 1, y))
                if x < self.grid_columns - 1:
                    neighbors.append((x + 1, y))
                if y > 0:
                    neighbors.append((x, y - 1))
                if y < self.grid_rows - 1:
                    neighbors.append((x, y + 1))
                graph[(x, y)] = neighbors
        return graph

    def remove_blocked_edges(self):
        for coord1, coord2 in self.blocked_edges.items():
            self.remove_edge(coord1, coord2)  # removes both directions

    def remove_edge(self, coord1, coord2):
        if coord2 in self.graph[coord1]:
            self.graph[coord1].remove(coord2)
        if coord1 in self.graph[coord2]:
            self.graph[coord2].remove(coord1)

    def visualize_graph(self):
        for y in range(self.grid_rows + 1):
            for x in range(self.grid_columns + 1):
                val = "P" if any((x, y) == package.source for package in self.packages) else "#"
                space = ""
                if x < self.grid_columns:
                    space = " - "
                print(val + space, end="")
            print()
            if y < self.grid_rows:
                print("|\t" * (self.grid_columns + 1))
