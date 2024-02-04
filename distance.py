from itertools import product
from functools import reduce
from math import inf

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