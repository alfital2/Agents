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
            node.grid.print_grid()
            print("List of moves so far:")
            temp = node
            while temp!=None:
                print(temp.current_position,end=" ")
                print("<-", end=" ")
                temp = temp.parent

            print("\nPoints of interest:{}".format(node.points_of_interest))

            print("\n--------------------------------------")
            if Node.goal_test(node): return node
            if Node.temp_goal_test(node):
                successors = node.get_successors()
                for move in successors:
                    new_node = node.make_node(move)
                    if new_node not in min_heap:
                        min_heap.enqueue(new_node)
                    else:
                        for n in min_heap:
                            if new_node==n and new_node.g_val+new_node.h_val < n.g_val+n.h_val:
                                min_heap.remove(n)
                                min_heap.enqueue(new_node)
                                break
            if not min_heap.is_empty():  # not empty
                next_state = min_heap.dequeue()
                return a_star(next_state)
            else:
                return None
        
        def a_star_iterative():
            while not min_heap.is_empty():
                node = min_heap.dequeue()
                # node.grid.print_grid()
                # print("List of moves so far:")
                # temp = node
                # while temp!=None:
                #     print(temp.current_position,end=" ")
                #     print("<-", end=" ")
                #     temp = temp.parent

                # print("\nPoints of interest:{}".format(node.points_of_interest))
                # print("h:{}, g:{}".format(node.h_val,node.g_val))
                # print("\n--------------------------------------")
                if Node.goal_test(node): return node
                if Node.temp_goal_test(node):
                    successors = node.get_successors()
                    for move in successors:
                        new_node = node.make_node(move)
                        # min_heap.enqueue(new_node)
                        if new_node not in min_heap:
                            min_heap.enqueue(new_node)
                        else:
                            for n in min_heap:
                                if new_node==n and new_node.g_val+new_node.h_val < n.g_val+n.h_val:
                                    min_heap.remove(n)
                                    min_heap.enqueue(new_node)
                                    break
            return None

        new_grid = copy.deepcopy(grid) #grid.copy()
        history = copy.deepcopy(self._package_history)
        node = Node(grid = new_grid,parent = None,cost=0,current_pos=self._pos, path=self._path,history=history)

        # Iterative:
        min_heap.enqueue(node)
        answer = a_star_iterative()

        # Recursive
        # answer = a_star_iterative(node)

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
            self._package_history[next_move] = {'obj': package, 'pick_up_time': grid.time+1, 'delivery_time': -1}
        destinations = {package['obj'].destination:coordinates for coordinates,package in self._package_history.items()}
        if next_move in destinations and self._package_history[destinations[next_move]]['delivery_time']==-1:
            self._package_history[destinations[next_move]]['delivery_time'] = grid.time+1
        return next_move
