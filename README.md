
# Logic Puzzle Solver

This project provides a set of Python scripts to solve various logic puzzles, including classic and custom challenges. Each puzzle is implemented in a separate file, and solutions are computed using constraint programming.

## Available Puzzles

- **Puzzle 1:** Classic logic puzzle (`main.py`)
- **Puzzle 2:** Second logic puzzle (`main2.py`)
- **Custom Puzzle:** User-defined logic puzzle (`main3.py`)
- **Zebra Puzzle:** Famous Zebra puzzle (`main4.py`)

## How to Run

Use Python 3 to execute the scripts:

- **Puzzle 1:**  
    `python main.py -a 5 -f 5 -d 5 -t 5`
- **Puzzle 2:**  
    `python main2.py -m 5 -p 5 -ha 5 -pri 5`
- **Custom Puzzle:**  
    `python main3.py`
- **Zebra Puzzle:**  
    `python main4.py`

Add the `-as` argument to display all possible solutions instead of just one.  
Example: `python main4.py -as`

## Notes

- To remove clues and see their effect, comment out the `clue(model)` calls in the `solve()` function of the puzzle files.
- When using `-as`, solutions are grouped by grid: all results for grid 1, then grid 2, and so on. Solution 1 of grid 1 matches solution 1 of grids 2 and 3, etc.


