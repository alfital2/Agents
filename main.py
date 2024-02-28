import file_parser
import Simulator
from node import Node
from heuristic_mst import heuristic_mst, goal_test_mst, should_explored_node
import sys


def choose_game_mode():
    print("Choose game mode:")
    print("1) Adversarial")
    print("2) Semi-cooperative")
    print("3) Fully-cooperative\n")

    while True:
        try:
            mode = int(input("Enter the number corresponding to your choice: "))
            if mode in [1, 2, 3]:
                return mode
            else:
                print("Invalid input. Please enter a number between 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    file_path = "environments/env1.txt"
    parser = file_parser.Parser(file_path)
    parser.parse()
    mode = choose_game_mode()
