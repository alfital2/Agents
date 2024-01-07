import file_parser
import Simulator


def main():
    file_path = "environments/env1.txt"
    parser = file_parser.Parser(file_path)
    parser.parse()

    grid_data = parser.get_grid_data()
    app_grid = grid.GridGraph(grid_data)


if __name__ == "__main__":
    main()
