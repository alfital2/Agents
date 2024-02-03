from node import Node


def a_star(min_heap):
    closed = []
    while True:
        if min_heap.is_empty():
            return None
        node = min_heap.dequeue()
        if Node.goal_test(node):
            return node
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
