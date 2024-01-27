from itertools import combinations

def heuristic_mst(state_node):
    def mst(nodes, edges):
        tree = set()
        visited = set()

        edges = sorted(edges, key=lambda x: x[2])

        while len(visited) != len(nodes):
            for edge in edges:
                if edge[0] not in visited or edge[1] not in visited:
                    visited.add(edge[0])
                    visited.add(edge[1])
                    tree.add(edge)
        return tree
    current_position = [state_node.current_position]
    pickable_packages = [package for package in state_node.grid.packages_position]
    deliverable_packages = [package['obj'].destination for coordinates, package in state_node.package_history.items() if package['delivery_time']==-1]
    graph_nodes = set(current_position + pickable_packages + deliverable_packages)
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
        answer = answer and spawn_time<=pick_up_time and delivery_time!=-1 and delivery_time<=final_time
    return answer