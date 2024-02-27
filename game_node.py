import copy


class Game_Node:
    heuristic = lambda x: 0
    goal_test = lambda x: False
    should_explored_node = lambda x: False

    def __init__(self, grid, parent, cost, agent, opponent, path, history={}):
        self.grid = grid
        self.parent = parent
        self.g_val = cost
        self.agent = agent
        self.opponent = opponent
        self.package_history = history
        self.path = set(path)
        pickup_packages = {x for x in grid.packages_position}  # collect all package sources on the grid
        destinations_packages = {x for x in grid.packages_destination}  # collect all packages destination
        general_points_of_interest = pickup_packages.union(destinations_packages)
        destinations_of_picked_up = {package['obj'].destination for _, package in self.package_history.items() if
                                     package['delivery_time'] == -1}
        self.points_of_interest = general_points_of_interest.union(
            destinations_of_picked_up)  # .union(destinations_of_not_pickedup)
        self.h_val = Game_Node.heuristic(self)

    def get_successors(self):
        return [move for move in self._get_moves() if self.grid.is_legal_move(self.agent.get_position(), move)] + [
            self.agent.get_position()]
    
    def get_score(self):
        return len(filter(lambda package:package['delivery_time'] != -1, self.package_history))

    def _get_moves(self):
        current_position = self.agent.get_position()
        left, right = (current_position[0] - 1, current_position[1]), (
            current_position[0] + 1, current_position[1])
        up, down = ((current_position[0], current_position[1] - 1),
                    (current_position[0], current_position[1] + 1))
        return [left, right, up, down]

    def expand(self, target):
        move_cost = 1  # self.grid.get_cost(self.current_position, target)
        new_grid = self.grid.move(self.agent.get_position(), target)
        new_grid.time += 1
        history = copy.deepcopy(self.package_history)

        if target in self.grid.packages_position:
            package = None
            for p in self.grid.packages_data:
                if p.source == target:
                    package = p
                    break
            history[target] = {'obj': package, 'pick_up_time': new_grid.time, 'delivery_time': -1}

        destinations = {package['obj'].destination: coordinates for coordinates, package in
                        history.items()}

        if target in destinations and self.package_history[destinations[target]]['delivery_time'] == -1:
            history[destinations[target]]['delivery_time'] = new_grid.time

        return Game_Node(grid=new_grid, parent=self, cost=self.g_val + move_cost, agent=self.opponent, opponent=self.agent,
                    path=self.path | {target}, history=history)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Game_Node):
            return False
        if self.agent.get_position() != other.agent.get_position():
            return False
        if self.points_of_interest != other.points_of_interest:
            return False
        if set(self.package_history.keys()) != set(other.package_history.keys()):
            return False
        for package in self.package_history:
            if self.package_history[package]['delivery_time'] * other.package_history[package]['delivery_time'] < 0:
                return False
        if self.grid.time != other.grid.time:
            return False
        return self.grid == other.grid
