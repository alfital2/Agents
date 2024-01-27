class Node:
    heuristic = lambda x: 0
    goal_test = lambda x: False

    def __init__(self, grid, parent, cost, current_pos, history = {}):
        self.grid = grid
        self.parent = parent
        self.g_val = cost
        self.current_position = current_pos
        self.h_val = Node.heuristic(self)
        self.package_history = history

    def make_node(self, target):
        move_cost = self.grid.get_cost(self.current_position, target)
        new_grid = self.grid.move(self.current_position, target)
        new_grid.time += 1

        if target in new_grid.packages_position:
            package = None
            for p in new_grid.packages_data:
                if p.source==target:
                    package = p
                    break
            self.package_history[target] = {'obj':package, 'pick_up_time':new_grid.time, 'delivery_time':-1}
            
        return Node(grid=new_grid, parent=self, cost=self.g_val + move_cost, current_pos=target)
