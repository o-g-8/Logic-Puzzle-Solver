import argparse
import itertools
import sys
import time
from datetime import timedelta
from typing import TextIO

from minizinc import Instance, Model, Solver, Result, Status
from observer import Observable
import labels3 as lbl

class Puzzle(Observable):
    def __init__(self, argv: argparse.Namespace):
        super().__init__()
        self.n_person: int = 3
        self.n_object: int = 3
        self.n_place: int = 3
        self.constraints = []
        self.clues = []

        self.find_all_solutions: bool = argv.all_solutions


        self.model: Model = Model("minizinc_model/Puzzle3.mzn")
        self.solver: Solver = Solver.lookup("gecode")
        self.solve()
    
    def print_result(self,result: list,name) -> None:
        
        if name == "P1":
            print("P1 RESULT |",end=" ")
            for i in range(self.n_object):
                print("Object"+str(i), end=" | ")
            print()

        else:
            print("P2 RESULT |",end=" ")
            for i in range(self.n_place):
                print("Place "+str(i), end=" | ")
            print()
        for i in range(0, len(result)):
            print("Person "+str(i), end="")

            for j in range(0, len(result[i])):
                print(" |", result[i][j], end="")
            print()


    def solve(self):
        model = Model("minizinc_model/Puzzle3.mzn")

        for i in self.clues:
            model.add_string(i)

        for i in self.constraints:
            model.add_string(i)

        instance: Instance = Instance(self.solver, model)
        instance["P"] = self.n_person
        instance["O"] = self.n_object
        instance["Pl"] = self.n_place

        result: Result = instance.solve(all_solutions=self.find_all_solutions)

        if result.status == Status.ALL_SOLUTIONS:
            solutionP1: list = [result.solution[i].P1 for i in range(len(result.solution))]
            solutionP2: list = [result.solution[i].P2 for i in range(len(result.solution))]
        elif result.status == Status.SATISFIED:
            solutionP1: list = result.solution.P1
            solutionP2: list = result.solution.P2
        else:
            solutionP1: list = []
            solutionP2: list = []

        self.print_solve_result(solutionP1,result,"P1")
        self.print_solve_result(solutionP2,result,"P2")
        print("Number of solutions:", len(solutionP1) if result.status == Status.ALL_SOLUTIONS else 1 if result.status == Status.SATISFIED else 0)
        print("Solving time:", result.statistics['flatTime'].total_seconds(), "seconds")
        
    def print_solve_result(self,solution,result,name):
        if result.status == Status.ALL_SOLUTIONS:
            for i in range(len(solution)):
                print()
                print("Solution : ", i + 1, "\n")
                self.print_result(solution[i],name)

        elif result.status == Status.SATISFIED:
            print()
            print("Solution\n")
            self.print_result(solution,name)

        else:
            print("No solution found")

    
    def add_constraint(self,constraint):
        self.constraints.append(constraint)
    
    def replace_constraint(self,old_constraint,new_constraint):
        for i in range(len(self.constraints)):
            if self.constraints[i] == old_constraint:
                self.constraints[i] = new_constraint
                break
    
    def remove_constraint(self,constraint):
        self.constraints.remove(constraint)

    def add_clue(self):
        for i in self.clues:
            self.model.add_string(i)
        clue_name = input("Enter the description of your clue : ")
        self.notify_observers(clue_name)
    
    def reset_clues(self):
        self.clues = []






