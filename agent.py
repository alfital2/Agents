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
            successors = node.get_successors()
            for move in successors:
                new_node = node.make_node(move)
                min_heap.enqueue(new_node)
            if not min_heap.is_empty():  # not empty
                next_state = min_heap.dequeue()
                return a_star(next_state)
            else:
                return None
        
        new_grid = copy.deepcopy(grid)
        history = copy.deepcopy(self._package_history)
        node = Node(grid = new_grid,parent = None,cost=0,current_pos=self._pos,history=history)
        answer = a_star(node)

        if answer.parent is None: # Already solved problem
            return None # TODO Should be check in get_action invoke
        
        while answer.parent.parent != None:# Grandparent is None: Parent->Son is the next move(aka Son.current_pos)
            answer = answer.parent

        next_move = answer.current_position
        self._path.append(next_move)
        self._pos = next_move
        if next_move in grid.packages_position:
            package = None
            for p in grid.packages_data:
                if p.source == next_move:
                    package = p
                    break
            self._package_history[next_move] = {'obj': package, 'pick_up_time': new_grid.time, 'delivery_time': -1}
        destinations = {package['obj'].destination:coordinates for coordinates,package in self._package_history.items()}
        if next_move in destinations and self._package_history[destinations[next_move]]['delivery_time']==-1:
            self._package_history[destinations[next_move]]['delivery_time'] = grid.time+1
        return next_move
