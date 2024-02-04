from node import Node
from fringe import Fringe
import copy
import logic


class Agent:
    def __init__(self, position) -> None:
        self._pos = position
        self._objectives = []
        self._path = []
        self._package_history = {}
        self.score = 0

    def get_position(self):
        return self._pos

    def get_action(self, grid):
        min_heap = Fringe(lambda x: x.g_val + x.h_val)
        new_grid = copy.deepcopy(grid)  # grid.copy()
        node = Node(grid=new_grid, parent=None, cost=0, current_pos=self._pos, path=self._path,
                    history=copy.deepcopy(self._package_history))
        if len(node.points_of_interest) == 0:
            return 1, None # success
        min_heap.enqueue(node)
        answer = logic.a_star(min_heap)
        if answer is None :
            return -1, None  # failed to find path

        next_move = self.extract_next_move(answer)
        self.acquire_package(grid, next_move)
        self.deliver_package(grid, next_move)
        return 0, next_move

    def deliver_package(self, grid, next_move):
        destinations = {package['obj'].destination: coordinates for coordinates, package in
                        self._package_history.items()}
        if next_move in destinations and self._package_history[destinations[next_move]]['delivery_time'] == -1:
            self._package_history[destinations[next_move]]['delivery_time'] = grid.time + 1
            self.score += 1

    def acquire_package(self, grid, next_move):
        if next_move in grid.packages_position:
            package = None
            for p in grid.packages_data:
                if p.source == next_move:
                    package = p
                    break
            self._package_history[next_move] = {'obj': package, 'pick_up_time': grid.time + 1, 'delivery_time': -1}

    def extract_next_move(self, answer):
        while answer.parent.parent is not None:  # Grandparent is None: Parent->Son is the next move(aka Son.current_pos)
            answer = answer.parent
        next_move = answer.current_position
        self._path.append(next_move)
        self._pos = next_move
        return next_move
