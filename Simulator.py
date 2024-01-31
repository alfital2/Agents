import grid
import time

class Simulator:

    def __init__(self, data):
        self.simulation_data = data
        self.agents = self.simulation_data["agents"]
        self.world = grid.Grid(self.simulation_data)

    def run(self):
        print("======MAPD SIMULATOR======")
        self.world.print_grid()
        solved = False
        while not solved:
            for agent in self.agents:
                current_position = agent.get_position()
                move = agent.get_action(self.world)
                if move is None:
                    solved = True
                    break # TODO is this necessary ? maybe return ?
                self.world = self.world.move(current_position,move)
                print("Real Move")
                self.world.print_grid()
                time.sleep(1)
            self.world.time += 1

#(1, 3) <- (1, 2) <- (1, 1) <- (2, 1) <- (3, 1) <- (4, 1) <- (4, 0) <- (4, 1) <- (4, 2) <- (4, 3) <- (3, 3) <- (2, 3) <- (1, 3) <- (0, 3) <- (0, 2) <- (0, 1) <- (0, 0) <-

def new_simulation(env_path):
    return Simulator(env_path)
