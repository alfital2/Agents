import file_parser
import Simulator as S
from node import Node
from heuristic_mst import heuristic_mst, goal_test_mst, should_explored_node
import sys


if __name__ == "__main__":
    file_path = "environments/env1.txt"
    parser = file_parser.Parser(file_path)
    parser.parse()

    Node.heuristic = heuristic_mst
    Node.goal_test = goal_test_mst
    Node.should_explored_node = should_explored_node
    simulator = S.new_simulation(parser.get_data())
    simulator.run()

    print("ended!")
