import edges
import packages


class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = {}

    def parse(self):
        packages_arr = []
        edges_arr = []
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                element = line.strip().split(' ')
                if element[0] == '#X':
                    x = int(element[1])
                elif element[0] == '#Y':
                    y = int(element[1])
                elif element[0] == '#P':
                    packages_arr.append(
                        packages.Package(tuple(element[1:3]), element[3], tuple(element[4:6]), element[6]))
                elif element[0] == '#B':
                    edges_arr.append(edges.BlockedEdge(element[1], element[2], element[3], element[4]))
                elif element[0] == '#F':
                    edges_arr.append(edges.FragileEdge(element[1], element[2], element[3], element[4]))

        self._data["grid_rows"] = y
        self._data["grid_columns"] = x
        self._data["packages"] = packages_arr
        self._data["edges"] = edges_arr

    def get_grid_data(self):
        return self._data
