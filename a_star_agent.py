from fringe import Fringe
from search_agent import Search_Agent


class A_Star_Agent(Search_Agent):
    def __init__(self, position) -> None:
        super().__init__(position)

    def init_fringe(self):
        return Fringe(lambda x: x.g_val + x.h_val)
