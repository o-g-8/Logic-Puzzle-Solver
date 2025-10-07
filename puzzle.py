import argparse
import itertools
import sys
import time
from datetime import timedelta
from typing import TextIO

from minizinc import Instance, Model, Solver, Result, Status
from observer import Observable
import labels as lbl

class Puzzle(Observable):
    def __init__(self, argv: argparse.Namespace):
        super().__init__()
        self.n_actor: int = argv.actor
        self.n_film: int = argv.film
        self.n_day: int = argv.day
        self.n_time: int = argv.time
        self.constraints = []

        self.find_all_solutions: bool = argv.all_solutions

        """
        log: bool = argv.log
        """
        self.model: Model = Model("minizinc_model/Puzzle1.mzn")
        self.solver: Solver = Solver.lookup("gecode")
        self.solve()
        
        """

        if log:
            current_time: str = str(time.strftime("%Y-%m-%d_%H-%M-%S"))

            symmetry: str = "_sym" if symmetry_breaking else ""
            all_solutions: str = "_all" if find_all_solutions else ""

            file: TextIO = open("../log/solution" +
                                "_w" + str(n_weeks) + "_g" + str(n_groups) + "_p" + str(n_participants) +
                                symmetry + all_solutions + "_" + current_time + ".txt", "a")

            default_stdout = sys.stdout
            sys.stdout = file
        """
    
    def print_result(self,result: list,name) -> None:
        
        if name == "P1":
            print("P1 RESULT |",end=" ")
            for i in range(self.n_film):
                print(lbl.film_labels[i], end=" | ")
            print()

        else:
            if name == "P2":
                print("P2 RESULT |",end=" ")
                for i in range(self.n_day):
                    print(lbl.day_labels[i], end=" | ")
                print()
            else:
                print("P3 RESULT |",end=" ")
                for i in range(self.n_time):
                    print(lbl.time_labels[i], end=" | ")
                print()
        for i in range(0, len(result)):
            print(lbl.actor_labels[i], end="")

            for j in range(0, len(result[i])):
                print(" |", result[i][j], end="")
            print()

    
    def solve(self):
        model = Model("minizinc_model/Puzzle1.mzn")
        lbl.clue1(model)
        lbl.clue2(model)
        lbl.clue3(model)
        lbl.clue4(model)
        lbl.clue5(model)
        lbl.clue6(model)
        lbl.clue7(model)
        for i in self.constraints:
            model.add_string(i)

        instance: Instance = Instance(self.solver, model)
        instance["A"] = self.n_actor
        instance["F"] = self.n_film
        instance["D"] = self.n_day
        instance["T"] = self.n_time

        result: Result = instance.solve(all_solutions=self.find_all_solutions)

        if result.status == Status.ALL_SOLUTIONS:
            solutionP1: list = [result.solution[i].P1 for i in range(len(result.solution))]
            solutionP2: list = [result.solution[i].P2 for i in range(len(result.solution))]
            solutionP3: list = [result.solution[i].P3 for i in range(len(result.solution))]
        elif result.status == Status.SATISFIED:
            solutionP1: list = result.solution.P1
            solutionP2: list = result.solution.P2
            solutionP3: list = result.solution.P3
        else:
            solutionP1: list = []
            solutionP2: list = []
            solutionP3: list = []

        self.print_solve_result(solutionP1,result,"P1")
        self.print_solve_result(solutionP2,result,"P2")
        self.print_solve_result(solutionP3,result,"P3")
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





