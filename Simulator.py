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

        while True:
            print("==============================")
            sum_status = 0
            print("World time:{}".format(self.world.time))
            for i,agent in enumerate(self.agents):
                current_position = agent.get_position()
                status, action = agent.get_action(self.world)
                sum_status += status
                if status == 0 and action != current_position:
                    self.world = self.world.move(current_position, action)
                    #print("Real Move")  # print world state
                    self.world.print_grid()
                    print("Agent {} moved to {}\n".format(i, action))
            self.world.time += 1
            [print("---Agent {} score is: {}---".format(i, agent.score)) for i,agent in enumerate(self.agents)]
            if sum_status == len(self.agents):
                return "success"
            elif sum_status == -len(self.agents):
                return "failure"
            print("\n")

    print()


def new_simulation(env_path):
    return Simulator(env_path)
