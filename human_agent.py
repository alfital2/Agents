class HumanAgent:
    def __init__(self, position):
        self._pos = position

    def getAction(self, grid):
        while True:
            x, y = input("I'm at {}\n Where do you wanna go?(format: X Y):".format(self._pos)).split()
            try:
                move = int(x), int(y)
            except ValueError:
                print("Wrong input, try again!")
                continue
            if not grid.isLegal(self._pos, move):
                print("Illegal move, try again!")
                continue
            self._pos = move
            return move