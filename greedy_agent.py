from search_agent import Search_Agent


class Greedy_Agent(Search_Agent):
    def __init__(self, position):
        super().__init__(position)
        self.search_limit = 1
