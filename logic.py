from node import Node
from game_node import Game_Node
from math import inf

def a_star(min_heap,limit):
    closed = []
    while True:
        if min_heap.is_empty():  # no solution
            return None, len(closed)
        node = min_heap.dequeue()
        if Node.goal_test(node):
            return node, len(closed)
        if node.g_val > limit:
            return node, len(closed)
        if Node.should_explored_node(node):
            try:
                i = closed.index(node)
                if node.g_val + node.h_val < closed[i].g_val + closed[i].h_val:
                    closed.pop(i)
                    closed.append(node)
                    min_heap.enqueue_all(node.expand(move) for move in node.get_successors())
            except ValueError:
                closed.append(node)
                min_heap.enqueue_all(node.expand(move) for move in node.get_successors())

def minmax(node, prune = False):
    def max_val(node, alpha = -inf, beta = inf):
        if Game_Node.goal_test(node):
            return node.get_score() - node.parent.get_score()
        val = -inf
        for move in node.get_successors():
            successor = node.expand(move)
            val = max(val, min_val(successor, alpha, beta))
            if prune:
                if val>=beta:
                    return val
                alpha = max(alpha, val)
        return val

    def min_val(node, alpha = -inf, beta = inf):
        if Game_Node.goal_test(node):
            return -node.get_score() + node.parent.get_score()
        val = inf
        for move in node.get_successors():
            successor = node.expand(move)
            val = min(val, max_val(successor, alpha, beta))
            if prune:
                if val<=alpha:
                    return val
                beta = min(beta, val)
        return val
    
    optimal_val = -inf
    optimal_succesor = None
    for move in node.get_successors():
        successor = node.expand(move)
        val = min_val(successor)
        if val > optimal_val:
            optimal_val = val
            optimal_succesor = successor
    return optimal_succesor
    




def debug(node):
    node.grid.print_grid()
    print("List of moves so far:")
    temp = node
    if temp is not None:
        print(temp.current_position, end=" ")
    temp = temp.parent

    while temp is not None:
        print("<-", end=" ")
        print(temp.current_position, end=" ")
        temp = temp.parent

    print("\nPoints of interest:{}".format(node.points_of_interest))
    print("h_val: ", node.h_val, " g_val: ", node.g_val)
    print("\n--------------------------------------")
