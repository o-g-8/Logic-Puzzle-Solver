import argparse
import itertools
import sys
import time
import tkinter as tk

from datetime import timedelta
from typing import TextIO

from minizinc import Instance, Model, Solver, Result, Status

from puzzle3 import Puzzle

from controller3 import Controller
from view3 import View


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Logic Puzzle 3',
        description='')
    
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