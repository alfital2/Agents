from node import Node
from fringe import Fringe
import copy

class Agent:
    def __init__(self, position) -> None:
        self._pos = position
        self._objectives = []
        self._path = []
        self._package_history = {}

    def _scan_objectives(self, grid) -> bool:
        # Scan for objectives and return if found any
        return False

    def _calc_path(self, grid) -> bool:
        # Calc path to 1st objective and return if exists
        pass

    def get_position(self):
        return self._pos

    def _get_moves(self):
        left, right = (self._pos[0] - 1, self._pos[1]), (self._pos[0] + 1, self._pos[1])
        up, down = (self._pos[0], self._pos[1] - 1), (self._pos[0], self._pos[1] + 1)
        return [left, right, up, down]

    def _calc_successor_function(self, node):
        return [move for move in self._get_moves() if node.grid.is_legal_move(self._pos, move)]

    def get_action(self, grid):
        min_heap = Fringe(lambda x: x.g_val + x.h_val)

        def a_star(node):
            if Node.goal_test(node): return node
            successors = self._calc_successor_function(node)
            for move in successors:
                new_node,self._objectives = node.make_node(move)
                min_heap.enqueue(new_node)
            if not min_heap.is_empty():  # not empty
                next_state = min_heap.dequeue()
                return a_star(next_state)
            else:
                return None
        
        new_grid = copy.deepcopy(grid)
        node = Node(grid = new_grid,parent = None,cost=0,current_pos=self._pos,history=self._package_history)
        answer = a_star(node)

        if answer.parent is None: # Already solved problem
            return None # TODO Should be check in get_action invoke
        
        while answer.parent.parent != None:# Grandparent is None: Parent->Son is the next move(aka Son.current_pos)
            answer = answer.parent
        
        self._path.append(answer.current_position)
        self._pos = answer.current_position
        return answer.current_position
