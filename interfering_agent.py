from stupid_agent import Stupid_Agent
from functools import reduce


class Interfering_Agent(Stupid_Agent):
    def __init__(self, position):
        super().__init__(position)

    def _get_interest_points(self, grid):
        fragile_edges_set = reduce(lambda x, y: x.union({y[0], y[1]}), grid.fragile_edges, set())
        curr_pos_set = {self._pos} # [(x,y),...]
        return fragile_edges_set-curr_pos_set

    def handle_package(self, grid, next_move):
        if {(self._pos, next_move),(next_move, self._pos)}&set(grid.fragile_edges):
            self.calc_score()

