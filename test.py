import argparse
import itertools
import sys
import time
from datetime import timedelta
from typing import TextIO

from minizinc import Instance, Model, Solver, Result, Status
from observer import Observable

class Puzzle(Observable):
    def __init__(self, argv: argparse.Namespace):
        super().__init__()
        self.n_actor: int = argv.actor
        self.n_film: int = argv.film
        self.n_day: int = argv.day
        self.n_time: int = argv.time
        print(self.n_time)
        self.constraints = []

        self.find_all_solutions: bool = argv.all_solutions

        """
        n_participants: int = argv.participants

        model: int = argv.model

        symmetry_breaking: bool = argv.symmetry_breaking

        log: bool = argv.log
        """
        result, status, flat_time = self.find_puzzle(self.find_all_solutions)
        
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

        if status == Status.ALL_SOLUTIONS:
            for i in range(len(result)):
                print("Solution", i + 1, "\n")
                self.print_result(result[i])

        elif status == Status.SATISFIED:
            print("Solution\n")
            self.print_result(result)

        else:
            print("No solution found")

        print("Number of solutions:",
                len(result) if status == Status.ALL_SOLUTIONS else 1 if status == Status.SATISFIED else 0)
        print("Solving time:", flat_time.total_seconds(), "seconds")
        """
        if log:
            file.close()
            sys.stdout = default_stdout

            print("Number of solutions:",
                    len(result) if status == Status.ALL_SOLUTIONS else 1 if status == Status.SATISFIED else 0)
            print("Solving time:", flat_time.total_seconds(), "seconds")
        """
    
    def print_result(self,result: list) -> None:
        for i in range(0, len(result)):
            print("Week", i, end="")

            for j in range(0, len(result[i])):
                print(" |", result[i][j], end="")

            print()

    def find_puzzle(self, find_all_solutions: bool) :
        self.model: Model = Model("/minizinc_model//Puzzle1.mzn")
        solver: Solver = Solver.lookup("gecode")

        instance: Instance = Instance(solver, self.model)
        instance["A"] = self.n_actor
        instance["F"] = self.n_film
        instance["D"] = self.n_day
        instance["T"] = self.n_time

        result: Result = instance.solve(all_solutions=find_all_solutions)

        if result.status == Status.ALL_SOLUTIONS:
            solution: list = [result.solution[i].P1 for i in range(len(result.solution))]
        elif result.status == Status.SATISFIED:
            solution: list = result.solution.P1
        else:
            solution: list = []

        return solution, result.status, result.statistics['flatTime']
    
    def solve(self):
        print("TEST")
        '''
        solver: Solver = Solver.lookup("gecode")

        instance: Instance = Instance(solver, self.model)
        instance["A"] = self.n_actor
        instance["F"] = self.n_film
        instance["D"] = self.n_day
        instance["T"] = self.n_time

        result: Result = instance.solve(all_solutions=self.find_all_solutions)

        if result.status == Status.ALL_SOLUTIONS:
            solution: list = [result.solution[i].P1 for i in range(len(result.solution))]
        elif result.status == Status.SATISFIED:
            solution: list = result.solution.P1
        else:
            solution: list = []

        

        if result.status == Status.ALL_SOLUTIONS:
            for i in range(len(result)):
                print("Solution", i + 1, "\n")
                self.print_result(result[i])

        elif result.status == Status.SATISFIED:
            print("Solution\n")
            self.print_result(result)

        else:
            print("No solution found")

        print("Number of solutions:",
                len(result) if result.status == Status.ALL_SOLUTIONS else 1 if status == Status.SATISFIED else 0)
        print("Solving time:", result.statistics['flatTime'].total_seconds(), "seconds")
        '''

    
    def add_constraint(self,constraint):
        self.constraints.append(constraint)
    
    def replace_constraint(self,old_constraint,new_constraint):
        for i in range(len(self.constraints)):
            if self.constraints[i] == old_constraint:
                self.constraints[i] = new_constraint
                break
    
    def remove_constraint(self,constraint):
        self.constraints.remove(constraint)





