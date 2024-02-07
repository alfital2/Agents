from agent import Agent


class HumanAgent(Agent):
    def __init__(self, position):
        super().__init__(position)

    def get_action(self, grid):
        while True:
            x, y = input("I'm at {}\n Where do you wanna go?(format: X Y):".format(self._pos)).split()
            try:
                move = int(x), int(y)
            except ValueError:
                print("Wrong input, try again!")
                continue
            if not grid.is_legal_move(self._pos, move):
                print("Illegal move, try again!")
                continue
            self._pos = move

            self.handle_package(grid,move)
            return move
