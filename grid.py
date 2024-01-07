class Grid:

    def __init__(self, data):
        self.grid_rows = data["grid_rows"]
        self.grid_columns = data["grid_columns"]
        self.packages = data["packages"]
        self.blocked_edges = data["blocked_edges"]
        self.fragile_edges = data["fragile_edges"]
        self.occupied_nodes = set()

    def is_legal_move(self, src, dst):
        return (self.is_open_path(src, dst) and
                self.is_node_not_occupied(dst) and
                self.is_move_in_grid_range(dst) and
                self.absolute_distance_is_max_one(src, dst)
                )

    def get_packages(self):
        return self.packages

    def is_move_in_grid_range(self, dst):
        return 0 <= dst[0] <= self.grid_columns and 0 <= dst[1] <= self.grid_rows

    def is_open_path(self, src, dst):
        return (src, dst) not in self.blocked_edges and (dst, src) not in self.blocked_edges

    def is_node_not_occupied(self, coordinates):
        return coordinates not in self.occupied_nodes

    def occupy_node(self, coordinates):
        self.occupied_nodes.add(coordinates)

    def release_occupied_node(self, coordinates):
        self.occupied_nodes.remove(coordinates)

    def is_fragile_edge(self, src, dst):
        return (src, dst) in self.fragile_edges or (dst, src) in self.fragile_edges

    def block_fragile_edge(self, src, dst):
        if tuple([src, dst]) in self.fragile_edges:
            self.fragile_edges.remove(tuple([src, dst]))
        else:
            self.fragile_edges.remove(tuple([dst, src]))
        self.blocked_edges.add(tuple([src, dst]))

    def move(self, src, dst):
        if self.is_legal_move(src, dst):
            if self.is_fragile_edge(src, dst):
                self.block_fragile_edge(src, dst)
            self.release_occupied_node(src)
            self.occupy_node(dst)
        else:
            raise IllegalMove("Invalid move, edge either blocked or destination node occupied")

    def absolute_distance_is_max_one(self, src, dst):
        x1, y1 = src
        x2, y2 = dst
        return abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1 and abs(x2 - x1) + abs(y2 - y1) <= 1


class GridErrors(Exception):
    pass


class IllegalMove(GridErrors):
    pass
