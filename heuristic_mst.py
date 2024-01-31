from itertools import combinations

def heuristic_mst(state_node):
    def mst(nodes, edges):
        tree = set()
        dss = {node:i for i,node in zip(range(len(nodes)),nodes)}
        #print(edges)
        edges = sorted(edges, key=lambda x: x[2])

        for edge in edges:
            g1, g2 = dss[edge[0]], dss[edge[1]]
            if g1!=g2:
                for node, i in dss.items():
                    if i==max(g1,g2):
                        dss[node] = min(g1,g2)
                tree.add(edge)
            if len(tree) == len(nodes) - 1:
                break
        return tree
    current_position = {state_node.current_position}
    graph_nodes = set(current_position | state_node.points_of_interest)
    graph_edges = []

    for n1, n2 in combinations(graph_nodes, 2):
        graph_edges.append((n1, n2, abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])))
    if len(graph_edges) == 0:
        return 0
    tree_weights = mst(graph_nodes, graph_edges)
    return sum([x[2] for x in tree_weights])


def goal_test_mst(state_node)->bool:
    pickable_packages = [package for package in state_node.grid.packages_position] # list of packages yet to be picked up
    answer = len(pickable_packages)==0 # checks if 0 pickable packages

    # For each package this agent interacted with check:
    #   if pickedup after spawn time
    #   if delivered before final time
    for package in state_node.package_history: 
        spawn_time = state_node.package_history[package]['obj'].delivery_time
        final_time = state_node.package_history[package]['obj'].max_delivery_time
        pick_up_time = state_node.package_history[package]['pick_up_time']
        delivery_time = state_node.package_history[package]['delivery_time']
        answer = answer and spawn_time<=pick_up_time and delivery_time!=-1 and delivery_time<=final_time and pick_up_time<delivery_time
    return answer

def temp_goal_test_mst(state_node)->bool:
    for package in state_node.package_history: 
        spawn_time = state_node.package_history[package]['obj'].delivery_time
        final_time = state_node.package_history[package]['obj'].max_delivery_time
        pick_up_time = state_node.package_history[package]['pick_up_time']
        delivery_time = state_node.package_history[package]['delivery_time']
        if pick_up_time<spawn_time or delivery_time>final_time:
            return False
    return True