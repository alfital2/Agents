import file_parser
import grid


class Simulator:

    def __init__(self, data):
        self.simulation_data = data
        self.agents = self.simulation_data["agents"]
        self.world = grid.Grid(self.simulation_data)
        self.time = 0

    def run(self):
        print("======MAPD SIMULATOR======")
        self.world.print_grid()
        while True:
            for agent in self.agents:
                current_position = agent.get_position()
                move = agent.get_action(self.world)
                self.world.move(current_position,move)
                self.world.print_grid()
                self.time = self.time + 1


def new_simulation(env_path):
    return Simulator(env_path)
