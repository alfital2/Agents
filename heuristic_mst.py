from itertools import combinations, product
from math import inf
from functools import reduce

def heuristic_mst(state_node):
    def mst(nodes, edges):
        tree = set()
        dss = {node: i for i, node in zip(range(len(nodes)), nodes)}
        # print(edges)
        edges = sorted(edges, key=lambda x: x[2])

        for edge in edges:
            g1, g2 = dss[edge[0]], dss[edge[1]]
            if g1 != g2:
                for node, i in dss.items():
                    if i == max(g1, g2):
                        dss[node] = min(g1, g2)
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

def manhattan(source, targets, grid):
    distances = {target:abs(source[0] - target[0]) + abs(source[1] - target[1]) for target in targets}
    distances[source] = 0
    return distances, None

def dijkstra(source, targets, grid): # stop after finding all targets
    path = {(x,y):None for x,y in product(range(grid.grid_columns+1),range(grid.grid_rows+1))}# check if +1 relevant
    distances = {(x,y):inf for x,y in product(range(grid.grid_columns+1),range(grid.grid_rows+1))}
    distances[source] = 0
    visited = set()
    
    d = sorted(filter(lambda x: x[0] not in visited, distances.items()), key=lambda x:x[1])

    while d or not reduce(lambda x,y:x and y,map(lambda x: distances[x]!=inf, targets),True):# fix non decreasing distances
        u, _ = d.pop(0)
        visited.add(u)

        potential_moves = [(u[0]-1,u[1]), (u[0]+1,u[1]), (u[0],u[1]-1), (u[0],u[1]+1)]
        neighbors = [move for move in potential_moves if grid.is_legal_move(u, move)]
        for v in neighbors:
            if v not in visited:
                if distances[v]>distances[u]+1:
                    distances[v]=distances[u]+1
                    path[v] = u

        d = sorted(d, key=lambda x:x[1])
    return distances, path


def goal_test_mst(state_node) -> bool:
    pickable_packages = [package for package in
                         state_node.grid.packages_position]  # list of packages yet to be picked up
    answer = len(pickable_packages) == 0  # checks if 0 pickable packages

    # For each package this agent interacted with check:
    #   if pickedup after spawn time
    #   if delivered before final time
    for package in state_node.package_history:
        spawn_time = state_node.package_history[package]['obj'].delivery_time
        final_time = state_node.package_history[package]['obj'].max_delivery_time
        pick_up_time = state_node.package_history[package]['pick_up_time']
        delivery_time = state_node.package_history[package]['delivery_time']
        answer = answer and spawn_time <= pick_up_time and delivery_time != -1 and delivery_time <= final_time and pick_up_time < delivery_time
    return answer


def should_explored_node(state_node) -> bool:
    for package in state_node.package_history:
        spawn_time = state_node.package_history[package]['obj'].delivery_time
        pickup_time = state_node.package_history[package]['pick_up_time']
        final_time = state_node.package_history[package]['obj'].max_delivery_time
        delivery_time = state_node.package_history[package]['delivery_time']
        if delivery_time > final_time or pickup_time<spawn_time:
            return False

    return not (max(package.max_delivery_time for package in state_node.grid.packages_data) < state_node.grid.time)
