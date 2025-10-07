import argparse
import itertools
import sys
import time
from datetime import timedelta
from typing import TextIO

from minizinc import Instance, Model, Solver, Result, Status
from observer import Observable
import labels4 as lbl

class Puzzle(Observable):
    def __init__(self, argv: argparse.Namespace):
        super().__init__()
        self.n_women: int = 5
        self.n_shirt: int = 5
        self.n_name: int = 5
        self.n_surname: int = 5
        self.n_pasta: int = 5
        self.n_wine: int = 5
        self.n_age: int = 5

        self.constraints = []

        self.find_all_solutions: bool = argv.all_solutions


        self.model: Model = Model("minizinc_model/Zebre.mzn")
        self.solver: Solver = Solver.lookup("gecode")
        self.solve()
    
    def print_result(self,result: list,name) -> None:
        
        if name == "P1":
            print("P1 RESULT |",end=" ")
            for i in range(self.n_shirt):
                print(lbl.shirt_labels[i], end=" | ")
            print()

        else:
            if name == "P2":
                print("P2 RESULT |",end=" ")
                for i in range(self.n_name):
                    print(lbl.name_labels[i], end=" | ")
                print()
            else:
                if name == "P3":
                    print("P3 RESULT |",end=" ")
                    for i in range(self.n_surname):
                        print(lbl.surname_labels[i], end=" | ")
                    print()
                else:
                    if name == "P4":
                        print("P4 RESULT |",end=" ")
                        for i in range(self.n_pasta):
                            print(lbl.pasta_labels[i], end=" | ")
                        print()
                    else:
                        if name == "P5":
                            print("P5 RESULT |",end=" ")
                            for i in range(self.n_wine):
                                print(lbl.wine_labels[i], end=" | ")
                            print()

                        else:
                            print("P6 RESULT |",end=" ")
                            for i in range(self.n_age):
                                print(lbl.age_labels[i], end=" | ")
                            print()

        for i in range(0, len(result)):
            print(lbl.women_labels[i], end="")

            for j in range(0, len(result[i])):
                print(" |", result[i][j], end="")
            print()

    
    def solve(self):
        model = Model("minizinc_model/Zebre.mzn")
        lbl.clue1(model)
        lbl.clue2(model)
        lbl.clue3(model)
        lbl.clue4(model)
        lbl.clue5(model)
        lbl.clue6(model)
        lbl.clue7(model)
        lbl.clue8(model)
        lbl.clue9(model)
        lbl.clue10(model)
        lbl.clue11(model)
        lbl.clue12(model)
        lbl.clue13(model)
        lbl.clue14(model)
        lbl.clue15(model)
        lbl.clue16(model)
        lbl.clue17(model)
        lbl.clue18(model)
        lbl.clue19(model)
        lbl.clue20(model)
        lbl.clue21(model)
        lbl.clue22(model)

        for i in self.constraints:
            model.add_string(i)

        instance: Instance = Instance(self.solver, model)


        result: Result = instance.solve(all_solutions=self.find_all_solutions)

        if result.status == Status.ALL_SOLUTIONS:
            solutionP1: list = [result.solution[i].P1 for i in range(len(result.solution))]
            solutionP2: list = [result.solution[i].P2 for i in range(len(result.solution))]
            solutionP3: list = [result.solution[i].P3 for i in range(len(result.solution))]
            solutionP4: list = [result.solution[i].P4 for i in range(len(result.solution))]
            solutionP5: list = [result.solution[i].P5 for i in range(len(result.solution))]
            solutionP6: list = [result.solution[i].P6 for i in range(len(result.solution))]
        elif result.status == Status.SATISFIED:
            solutionP1: list = result.solution.P1
            solutionP2: list = result.solution.P2
            solutionP3: list = result.solution.P3
            solutionP4: list = result.solution.P4
            solutionP5: list = result.solution.P5
            solutionP6: list = result.solution.P6
        else:
            solutionP1: list = []
            solutionP2: list = []
            solutionP3: list = []
            solutionP4: list = []
            solutionP5: list = []
            solutionP6: list = []

        self.print_solve_result(solutionP1,result,"P1")
        self.print_solve_result(solutionP2,result,"P2")
        self.print_solve_result(solutionP3,result,"P3")
        self.print_solve_result(solutionP4,result,"P4")
        self.print_solve_result(solutionP5,result,"P5")
        self.print_solve_result(solutionP6,result,"P6")
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





