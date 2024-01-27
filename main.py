import file_parser
import Simulator as S
from node import Node
from heuristic_mst import heuristic_mst


if __name__ == "__main__":
    file_path = "environments/env1.txt"
    parser = file_parser.Parser(file_path)
    parser.parse()

    Node.heuristic = heuristic_mst
    simulator = S.new_simulation(parser.get_data())
    simulator.run()
