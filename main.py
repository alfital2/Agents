import file_parser
import Simulator as S


if __name__ == "__main__":
    file_path = "environments/env1.txt"
    parser = file_parser.Parser(file_path)
    parser.parse()

    simulator = S.new_simulation(parser.get_data())
    simulator.run()
