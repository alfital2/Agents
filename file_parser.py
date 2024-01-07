import Coordinate
import packages


class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = {}

    def parse(self):
        packages_arr = []
        blocked_edges = {}
        fragile_edges = {}
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                element = line.strip().split(' ')
                if element[0] == '#X':
                    x = int(element[1])
                elif element[0] == '#Y':
                    y = int(element[1])
                elif element[0] == '#P':
                    src, dst = extract_coordinates(element[1:3] + element[6:8])
                    packages_arr.append(
                        packages.Package(src, element[3], dst, element[6]))
                elif element[0] == '#B':
                    x1y1, x2y2 = extract_coordinates(element[1:])
                    blocked_edges[x1y1] = x2y2
                elif element[0] == '#F':
                    x1y1, x2y2 = extract_coordinates(element[1:])
                    fragile_edges[x1y1] = x2y2
                    fragile_edges[x2y2] = x1y1

        self._data["grid_rows"] = y
        self._data["grid_columns"] = x
        self._data["packages"] = packages_arr
        self._data["blocked_edges"] = blocked_edges
        self._data["fragile_edges"] = fragile_edges

    def get_grid_data(self):
        return self._data


def extract_coordinates(element):
    x1y1 = (int(element[0]), int(element[1]))
    x2y2 = (int(element[2]), int(element[3]))
    return x1y1, x2y2
