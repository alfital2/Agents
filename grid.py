import edges, packages
from collections import defaultdict


class Grid:
    def __init__(self, data):

        self.grid_rows = data["grid_rows"]
        self.grid_columns = data["grid_columns"]
        self.packages = data["packages"]
        self.edges = data["edges"]
        self.grid_prototype = None

        self.generate_grid()

    def generate_grid(self):
        self.grid_prototype = [["#" for x in range(self.grid_columns+1)] for i in range(self.grid_rows+1)]

        for package in self.packages:
            self.grid_prototype[int(package.source[1])][int(package.source[0])] = "P"


    def print_grid(self):
        for x in range(len(self.grid_prototype)):
            for y in range(len(self.grid_prototype[0])):
                print(self.grid_prototype[x][y], end='\t')
            print("\n")
