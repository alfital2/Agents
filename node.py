from functools import reduce

import copy
class Node:
    heuristic = lambda x: 0
    goal_test = lambda x: False
    should_explored_node = lambda x :False
    node_id = 0

    def __init__(self, grid, parent, cost, current_pos, path, history = {}):
        self.grid = grid
        self.parent = parent
        self.g_val = cost
        self.current_position = current_pos
        self.package_history = history
        self.id = Node.node_id
        self.path = set(path)
        pickup_packages = {x for x in grid.packages_position} # collect all package sources on the grid
        destinations_packages = {x for x in grid.packages_destination} # collect all packages destination
        general_points_of_interest = pickup_packages.union(destinations_packages)
        # points_to_visit = general_points_of_interest.difference(self.path)

        # store all the destinations of packages that has already been picked up - but not delivered!
        destinations_of_pickedup = {package['obj'].destination for _, package in self.package_history.items() if package['delivery_time']==-1}

        # store all the packages that i do not have
        #destinations_of_delivered = {package['obj'].destination for _, package in self.package_history.items() if package['delivery_time']!=-1}
        #destinations_revisit = 

        self.points_of_interest = general_points_of_interest.union(destinations_of_pickedup)#.union(destinations_of_not_pickedup)
        self.h_val = Node.heuristic(self)
        Node.node_id+=1

    def get_successors(self):
        return [move for move in self._get_moves() if self.grid.is_legal_move(self.current_position, move)]+[self.current_position]

    def _get_moves(self):
        left, right = (self.current_position[0] - 1, self.current_position[1]), (self.current_position[0] + 1, self.current_position[1])
        up, down = ((self.current_position[0], self.current_position[1] - 1), (self.current_position[0], self.current_position[1] + 1))
        return [left, right, up, down]

    def make_node(self, target):
        move_cost = 1 #self.grid.get_cost(self.current_position, target)
        new_grid = self.grid.move(self.current_position, target)
        new_grid.time += 1
        history = copy.deepcopy(self.package_history)

        if target in self.grid.packages_position:
            package = None
            for p in self.grid.packages_data:
                if p.source==target:
                    package = p
                    break
            history[target] = {'obj':package, 'pick_up_time':new_grid.time, 'delivery_time':-1}

        destinations = {package['obj'].destination: coordinates for coordinates, package in
                        history.items()}
        
        if target in destinations and self.package_history[destinations[target]]['delivery_time'] == -1:
            history[destinations[target]]['delivery_time'] = new_grid.time


        return Node(grid=new_grid, parent=self, cost=self.g_val + move_cost, current_pos=target,path=self.path|{target},history=history)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return False
        if self.current_position != other.current_position:
            return False
        if self.points_of_interest != other.points_of_interest:
            return False
        if set(self.package_history.keys()) != set(other.package_history.keys()):
            return False
        for package in self.package_history:
            if self.package_history[package]['delivery_time']*other.package_history[package]['delivery_time']<0:
                return False
        if self.grid.time != other.grid.time:
            return False
        return self.grid == other.grid

