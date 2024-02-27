from a_star_agent import A_Star_Agent
import copy
from node import Node
import logic
from math import inf


class Game_Search_Agent(A_Star_Agent):
    def __init__(self, position):
        super().__init__(position)

    def get_action(self, grid):
        # TODO Redo according to game search agent
        
        min_heap = self.init_fringe()
        new_grid = copy.deepcopy(grid)  # grid.copy()
        node = Node(grid=new_grid, parent=None, cost=0, current_pos=self._pos, path=self._path,
                    history=copy.deepcopy(self._package_history))
        if len(node.points_of_interest) == 0:
            return 1, None  # success
        min_heap.enqueue(node)
        answer, expansions = logic.a_star(min_heap, self.search_limit)
        self._expansions += expansions
        if answer is None:
            return -1, None  # failed to find path

        next_move = self._extract_next_move(answer)
        self.handle_package(grid, next_move)
        return 0, next_move
