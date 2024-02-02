from node import Node


# def a_star(min_heap):
#     closed = set()
#     while not min_heap.is_empty():
#         node = min_heap.dequeue()
#         debug(node)
#         if Node.goal_test(node): return node
#         if Node.temp_goal_test(node):
#             successors = node.get_successors()
#             closed.add(node)
#             for move in successors:
#                 new_node = node.make_node(move)
#                 if new_node not in closed:
#                     min_heap.enqueue(new_node)
#                 else:
#                     for n in closed:
#                         if new_node == n and new_node.g_val + new_node.h_val < n.g_val + n.h_val:
#                             min_heap.remove(n)
#                             min_heap.enqueue(new_node)
#                             break
#     return None
#


def a_star(min_heap):
    closed = []
    exp = 1
    while True:
        if min_heap.is_empty():
            return None
        node = min_heap.dequeue()
        if Node.goal_test(node):
            return node
        # debug(node)
        if Node.should_explored_node(node):
            try:
                i = closed.index(node)
                # if node.g_val + node.h_val < closed[i].g_val + closed[i].h_val:
                #     print("fart!!!!")
                # if closed[i] == node and node:
                #     print("poop!!")
                #if closed[i] == node:
                if node.g_val + node.h_val < closed[i].g_val + closed[i].h_val:
                    closed.pop(i)
                    closed.append(node)
                    print("found identical node!!")
                    min_heap.enqueue_all(node.make_node(move) for move in node.get_successors())  # change func name to expend
                    # if node.g_val + node.h_val == closed[i].g_val + closed[i].h_val:
                    #     min_heap.enqueue_all(node.make_node(move) for move in node.get_successors())  # change func name to expend
            except ValueError:
                closed.append(node)
                min_heap.enqueue_all(node.make_node(move) for move in node.get_successors())  # change func name to expend
        else:
            print("not exploring node")
        if exp % 1000 == 0:
            print("expand num:", exp)
            print("g_val:",node.g_val)
        exp += 1

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
