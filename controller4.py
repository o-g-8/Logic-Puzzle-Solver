# controller.py
from puzzle4 import Puzzle

class Controller:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def add_constraint(self,constraint):
        self.puzzle.add_constraint(constraint)
    
    def replace_constraint(self,old_constraint,new_constraint):
        self.puzzle.replace_constraint(old_constraint,new_constraint)
    
    def remove_constraint(self,constraint):
        self.puzzle.remove_constraint(constraint)

    def solve(self):
        self.puzzle.solve()
        

    



