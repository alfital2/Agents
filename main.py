import file_parser
import Simulator
from node import Node
from heuristic_mst import heuristic_mst, goal_test_mst, should_explored_node


if __name__ == "__main__":
    file_path = "environments/2X2.txt"
    parser = file_parser.Parser(file_path)
    parser.parse()

    Node.heuristic = heuristic_mst
    Node.goal_test = goal_test_mst
    Node.should_explored_node = should_explored_node
    Simulator.Simulator.T = 0.1
    simulator = Simulator.new_simulation(parser.get_data())
    print(simulator.run())
