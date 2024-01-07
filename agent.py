class Agent:
    def __init__(self, position) -> None:
        self._pos = position
        self._objectives = []
        self._path = []
        
    def _scan_objectives(self, grid) -> bool:
        # Scan for objectives and return if found any
        return False

    def _calc_path(self, grid) -> bool:
        # Calc path to 1st objective and return if exists
        pass

    def get_position(self):
        return self._pos

    def get_action(self, grid):
        if not self._objectives:
            if not self._scan_objectives(grid):
                return None
            
        if not self._path:
            if not self._calc_path(grid):
                return None

        return self._path[0]