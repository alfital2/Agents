import file_parser
import grid


def main():
    file_path = "environments/env1.txt"
    parser = file_parser.Parser(file_path)
    parser.parse()

    grid_data = parser.get_grid_data()
    app_grid = grid.Grid(grid_data)
    app_grid.print_grid()

if __name__ == "__main__":
    main()
