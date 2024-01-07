from agent import Agent

class StupidAgent(Agent):
    def __init__(self, position):
        super.__init__(position)

    def _scan_objectives(self, grid) -> bool:
        # Scan for objectives and return if found any
        min_dist = grid.width + grid.height
        best_pack = None
        for package in grid.get_packages():
            dist = abs(package.source[0] - self._pos[0]) + abs(package.source[1] - self.pos[1])
            if dist < min_dist:
                best_pack = package
                min_dist = dist
        if best_pack:
            return True
        return False

    def _calc_path(self, grid) -> bool:
        # Calc path to 1st objective and return if exists
        pass

    def get_action(self, grid):
        if not self._objectives:
            if not self._scan_objectives(grid):
                return None
            
        if not self._path:
            if not self._calc_path(grid):
                return None

        return self._path[0]