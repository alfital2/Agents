class Node:
    def __init__(self,grid,parent,cost,current_pos):
        self.grid = grid
        self.parent = parent
        self.cost = cost
        self.current_pos = current_pos

   def make_node(self,target):
       move_cost = self.grid.get_cost(self.current_position, target)
       new_grid = self.grid.make_cloned_move(self.current_position, target)
       return Node(grid=new_grid,parent=self,cost = self.cost+ move_cost,current_pos=target)