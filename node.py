from functools import reduce

import copy
class Node:
    heuristic = lambda x: 0
    goal_test = lambda x: False

    def __init__(self, grid, parent, cost, current_pos, history = {}):
        self.grid = grid
        self.parent = parent
        self.g_val = cost
        self.current_position = current_pos
        self.package_history = history
        self.h_val = Node.heuristic(self)

    def get_successors(self):
        return [move for move in self._get_moves() if self.grid.is_legal_move(self.current_position, move)]

    def _get_moves(self):
        left, right = (self.current_position[0] - 1,
                       self.current_position[1]), (self.current_position[0] + 1, self.current_position[1])
        up, down = ((self.current_position[0], self.current_position[1] - 1),
                    (self.current_position[0], self.current_position[1] + 1))
        return [left, right, up, down]

    def make_node(self, target):
        move_cost = self.grid.get_cost(self.current_position, target)
        new_grid = self.grid.move(self.current_position, target)
        new_grid.time += 1

        if target in self.grid.packages_position:
            package = None
            for p in self.grid.packages_data:
                if p.source==target:
                    package = p
                    break
            self.package_history[target] = {'obj':package, 'pick_up_time':new_grid.time, 'delivery_time':-1}
        destinations = {package['obj'].destination: coordinates for coordinates, package in
                        self.package_history.items()}
        if target in destinations and self.package_history[destinations[target]]['delivery_time'] == -1:
            self.package_history[destinations[target]]['delivery_time'] = self.grid.time + 1
        history = copy.deepcopy(self.package_history)
        return Node(grid=new_grid, parent=self, cost=self.g_val + move_cost, current_pos=target,history=history)

    def __eq__(self, other) -> bool:
        if self.current_position!=other.current_position:
            return False
        for package in self.package_history:
            if package in other.package_history:
                for attr1, attr2 in zip(self.package_history[package], other.package_history[package]):
                    if self.package_history[package][attr1] != other.package_history[package][attr2]:
                        return False
            else:
                return False
        return self.grid == other.grid

