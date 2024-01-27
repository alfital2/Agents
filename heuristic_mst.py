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

    graph_nodes = [state_node.current_pos] + [package for package in
                                              state_node.grid.packages_position]  # TODO add package destinations
    graph_edges = []

    for n1, n2 in combinations(graph_nodes, 2):
        graph_edges.append((n1, n2, abs(n1[0] - n2[0]) + abs(n1[1] + n2[1])))

    tree_weights = mst(graph_nodes, graph_edges)
    return sum([x[2] for x in tree_weights])


def goal_test_mst(state_node):
