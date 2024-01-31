import file_parser
import Simulator as S
from node import Node
from heuristic_mst import heuristic_mst, goal_test_mst, temp_goal_test_mst
import sys


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    file_path = "environments/env3.txt"
    parser = file_parser.Parser(file_path)
    parser.parse()

    Node.heuristic = heuristic_mst
    Node.goal_test = goal_test_mst
    Node.temp_goal_test = temp_goal_test_mst
    simulator = S.new_simulation(parser.get_data())
    simulator.run()

    print("ended!")
