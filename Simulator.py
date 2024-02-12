import grid
from search_agent import Search_Agent
from interfering_agent import Interfering_Agent


class Simulator:
    T = 0

    def __init__(self, data):
        self.simulation_data = data
        self.agents = self.simulation_data["agents"]
        self.world = grid.Grid(self.simulation_data)

    def run(self):
        print("======MAPD SIMULATOR======")
        print("---initial world state:---")
        self.world.print_grid()

        while True:
            print("==============================")
            sum_status = 0
            print("World time:{}".format(self.world.time + 1))
            for i, agent in enumerate(self.agents):
                current_position = agent.get_position()
                status, action = agent.get_action(self.world)
                sum_status += status
                if status == 0:
                    if action != current_position:
                        if isinstance(action, Interfering_Agent):
                            self.world = self.world.move(current_position, action, False)
                        else:
                            self.world = self.world.move(current_position, action)
                        self.world.print_grid()
                        print("Agent {} moved to {}\n".format(i, action))
                    else:
                        self.world.print_grid()
                        print("Agent {} stayed in {}\n".format(i, action))
            self.world.time += 1
            [print("---Agent {} score is: {}---".format(i, agent.score)) for i, agent in enumerate(self.agents)]
            [print("---Search Agent {} current performance measure is: {}---".format(i, float(
                agent.get_current_expansions()) * Simulator.T))

             for i, agent in enumerate(self.agents) if isinstance(agent, Search_Agent)]
            if sum_status == len(self.agents):
                print("success")
                break
            elif sum_status == -len(self.agents):
                print("failure")
                break
            print("\n")
        print("Simulator.T: ", Simulator.T)
        [print("---Search Agent {} total performance measure is: {}---".format(i, float(
            agent.get_expansions()) * Simulator.T))

         for i, agent in enumerate(self.agents) if isinstance(agent, Search_Agent)]

    print()


def new_simulation(env_path):
    return Simulator(env_path)
