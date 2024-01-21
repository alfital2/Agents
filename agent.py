import node

class Agent:
    def __init__(self, position) -> None:
        self._pos = position
        self._objectives = []
        self._path = []
        
    def _scan_objectives(self, grid) -> bool:
        # Scan for objectives and return if found any
        return False

    def _calc_path(self, grid) -> bool:
        # Calc path to 1st objective and return if exists
        pass

    def get_position(self):
        return self._pos


    def _get_moves(self):
        left,right = (self._pos[0]-1,self._pos[1]),(self._pos[0]+1,self._pos[1])
        up, down = (self._pos[0],self._pos[1]-1),(self._pos[0],self._pos[1]+1)
        return [left,right,up,down]

    def _calc_successor_function(self,node):
        return [move for move in self._get_moves() if node.grid.is_legal_move(self._pos,move)]

    def get_action(self, grid, goal_test):

        def a_star(node):
            if goal_test(node): return node
            successors = self._calc_successor_function(node)
            for move in successors:
                new_node = node.make_node(move)
                h = calc_mst(new_node)
                queue.enqueue_and_sort(new_node)
            if not queue.is_empty():
                next_state = queue.dequeue()
                return a_star(next_state)
            else:
                return None


        if not self._objectives:
            if not self._scan_objectives(grid):
                return None
            
        if not self._path:
            if not self._calc_path(grid):
                return None

        return self._path[0]

    def mst_heuristic_value(self, grid): # TODO will add implementation later
        grid = grid
        return 0