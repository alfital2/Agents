from fringe import Fringe
from a_star_agent import A_Star_Agent


class RTA_Star_Agent(A_Star_Agent):
    def __init__(self, position,limit) -> None:
        super().__init__(position)
        self.search_limit = limit

