import argparse
import itertools
import sys
import time
import tkinter as tk

from datetime import timedelta
from typing import TextIO

from minizinc import Instance, Model, Solver, Result, Status

from puzzle2 import Puzzle

from controller2 import Controller
from view2 import View


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Logic Puzzle 2',
        description='Refer to https://www.ahapuzzles.com/logic/logic-puzzles/a-new-personal-computer/')

    parser.add_argument('-m', '--monitor', type=int, required=True,
                        help="Number of actors")
    parser.add_argument('-p', '--processor', type=int, required=True,
                        help="Number of films")
    parser.add_argument('-ha', '--harddisk', type=int, required=True,
                        help="Number of days")

    parser.add_argument('-pri', '--price', type=int, required=True,
                        help="Number of time")
    
    parser.add_argument('-as', '--all-solutions', action='store_true', default=False,
                        help="Flag to find all solutions of an instance (False by default)")

    args: argparse.Namespace = parser.parse_args()
    print(args)
    print()
    root = tk.Tk()
    puzzle = Puzzle(args)
    controller = Controller(puzzle)
    
    view = View(args, controller, puzzle,root)
    root.mainloop()