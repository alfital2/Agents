from stupid_agent import Stupid_Agent


class Stupid_Greedy_Agent(Stupid_Agent):
    def __init__(self, position):
        super().__init__(position)

    def _get_interest_points(self, grid):
        pickup_packages = {x for x in grid.packages_position}
        destinations_of_picked_up = {package['obj'].destination for _, package in self._package_history.items() if
                                     package['delivery_time'] == -1 and package['obj'].max_delivery_time > grid.time}
        return pickup_packages.union(destinations_of_picked_up)

    def _can_make_next_move(self, grid, move):
        if not super()._can_make_next_move(grid, move):
            return False
        if move in grid.packages_position:
            package = None
            for p in grid.packages_data:
                if p.source == move:
                    package = p
                    break
            if package.delivery_time>grid.time+1:
                return False
        return True
