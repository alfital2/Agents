from agent import Agent
from heuristic_mst import dijkstra
from math import inf

class Stupid_Agent(Agent):

    def __init__(self, position):
        super().__init__(position)

    def _get_interest_points(self, grid):
        return []

    def _extract_next_move(self, target, path):
        while path[target] != self._pos:
            target = path[target]
        return target

    def _can_make_next_move(self, grid, move):
        return grid.is_legal_move(self._pos, move)

    def get_action(self, grid):
        poi = self._get_interest_points(grid)
        if poi:
            distances, path = dijkstra(self._pos, poi, grid)
            poi_distances = dict(filter(lambda x: x[0] in poi, distances.items()))
            closest_poi = min(poi_distances, key=lambda x: poi_distances[x])
            if poi_distances[closest_poi] == inf:
                return -1, None
            next_move = self._extract_next_move(closest_poi, path)
            if next_move == closest_poi and not self._can_make_next_move(grid, next_move): # No-Op
                return 0, self._pos
            self.handle_package(grid, next_move)
            self._pos = next_move
            return 0, next_move
        else:
            for package in self._package_history:
                if self._package_history[package]['delivery_time'] == -1:
                    return -1, None
            return 1, None

    def handle_package(self, grid, next_move):
        self.acquire_package(grid, next_move)
        self.deliver_package(grid, next_move)


