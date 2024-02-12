from agent import Agent
from fringe import Fringe
import copy
from node import Node
import logic
from math import inf


class Search_Agent(Agent):
    def __init__(self, position):
        self.search_limit = inf
        self._expansions = 0
        self._current_expansions = 0
        super().__init__(position)

    def _extract_next_move(self, answer):
        while answer.parent.parent is not None:
            answer = answer.parent
        next_move = answer.current_position
        self._path.append(next_move)
        self._pos = next_move
        return next_move

    def init_fringe(self):
        return Fringe(lambda x: x.h_val)

    def get_expansions(self):
        return self._expansions

    def get_current_expansions(self):
        return self._current_expansions

    def get_action(self, grid):
        min_heap = self.init_fringe()
        new_grid = copy.deepcopy(grid)  # grid.copy()
        node = Node(grid=new_grid, parent=None, cost=0, current_pos=self._pos, path=self._path,
                    history=copy.deepcopy(self._package_history))
        if len(node.points_of_interest) == 0:
            return 1, None  # success
        min_heap.enqueue(node)
        answer, expansions = logic.a_star(min_heap, self.search_limit)
        self._current_expansions = expansions
        self._expansions += expansions
        if answer is None:
            return -1, None  # failed to find path

        next_move = self._extract_next_move(answer)
        self.handle_package(grid, next_move)
        return 0, next_move
