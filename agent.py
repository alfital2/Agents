class Agent:

    def __init__(self,position):
        self._pos = position
        self._path = []
        self._package_history = {}
        self.score = 0

    def get_position(self):
        return self._pos

    def acquire_package(self, grid, next_move):
        if next_move in grid.packages_position:
            package = None
            for p in grid.packages_data:
                if p.source == next_move:
                    package = p
                    break
            self._package_history[next_move] = {'obj': package, 'pick_up_time': grid.time + 1, 'delivery_time': -1}

    def deliver_package(self, grid, next_move):
        destinations = {package['obj'].destination: coordinates for coordinates, package in
                        self._package_history.items()}
        if next_move in destinations and self._package_history[destinations[next_move]]['delivery_time'] == -1:
            self._package_history[destinations[next_move]]['delivery_time'] = grid.time + 1
            if (self._package_history[destinations[next_move]]['delivery_time'] <=
                    self._package_history[destinations[next_move]]['obj'].max_delivery_time):
                self.calc_score()

    def calc_score(self):
        self.score += 1

    def handle_package(self, grid, next_move):
        self.acquire_package(grid, next_move)
        self.deliver_package(grid, next_move)
