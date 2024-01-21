class Grid:

    def __init__(self, data):
        self.grid_rows = data["grid_rows"]
        self.grid_columns = data["grid_columns"]
        self.packages_data = data["packages"]
        self.packages_position = {x.source for x in self.packages_data}
        self.blocked_edges = data["blocked_edges"]
        self.fragile_edges = data["fragile_edges"]
        self.agents_arr = data["agents"]
        self.occupied_nodes = set()  # only occupied be agents

        self.place_agents_on_grid()

    def is_legal_move(self, src, dst):
        return (self.is_open_path(src, dst) and
                self.is_node_not_occupied(dst) and
                self.is_move_in_grid_range(dst) and
                self.absolute_distance_is_max_one(src, dst)
                )

    def get_packages(self):
        return self.packages_data

    def place_agents_on_grid(self):
        agents_position = {x.get_position() for x in self.agents_arr}
        for position in agents_position:
            self.occupy_node(position)

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

    def is_blocked_edge(self, src, dst):
        return (src, dst) in self.blocked_edges or (dst, src) in self.blocked_edges

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
        return self.get_cost(src, dst) <= 1

    def get_cost(self, src, dst):
        x1, y1 = src
        x2, y2 = dst
        return abs(x2 - x1) + abs(y2 - y1)

    def print_grid(self):
        for row in range(self.grid_rows + 1):
            vertical_path = []
            for col in range(self.grid_columns + 1):
                item = "#"
                if (col, row) in self.packages_position:
                    item = "P"
                elif (col, row) in self.occupied_nodes:
                    item = "@"

                if self.is_blocked_edge((col, row), (col + 1, row)):
                    path = "\t"
                elif self.is_fragile_edge((col, row), (col + 1, row)):
                    path = " ~ "
                elif col == self.grid_columns:
                    path = ""
                else:
                    path = " - "
                print(item, end=path)

                if self.is_blocked_edge((col, row), (col, row + 1)):
                    vertical_path.append("\t")
                elif self.is_fragile_edge((col, row), (col, row + 1)):
                    vertical_path.append("Ξ\t")
                elif row == self.grid_rows:
                    vertical_path.append("")
                else:
                    vertical_path.append("|\t")
            print()
            print(''.join(vertical_path))


class GridErrors(Exception):
    pass


class IllegalMove(GridErrors):
    pass
