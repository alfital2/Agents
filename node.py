class Node:
    heuristic = lambda x: 0
    goal_test = lambda x: False

    def __init__(self, grid, parent, cost, current_pos):
        self.grid = grid
        self.parent = parent
        self.g_val = cost
        self.current_position = current_pos
        self.h_val = Node.heuristic(self)

    def make_node(self, target):
        move_cost = self.grid.get_cost(self.current_position, target)
        new_grid,collected_package = self.grid.move(self.current_position, target)
        # add destination (a point of interest on the grid)
        new_grid.time += 1
        return Node(grid=new_grid, parent=self, cost=self.g_val + move_cost, current_pos=target)
