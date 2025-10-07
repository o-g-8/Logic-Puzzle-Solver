import tkinter as tk
from tkinter import font
from observer import Observer
from controller4 import Controller

import labels4 as lbl

class View(Observer):
    def __init__(self, args, controller, observable, root):
        
        self.controller = controller
        self.puzzle = observable
        self.puzzle.add_observer(self)

        self.root = root
        self.root.title("Puzzle Zebre")
    

        self.n_women: int = 5
        self.n_shirt: int = 5
        self.n_name: int = 5
        self.n_surname: int = 5
        self.n_pasta: int = 5
        self.n_wine: int = 5
        self.n_age: int = 5

        self.grid_w_s = [[None for _ in range(5)] for _ in range(5)]
        self.grid_w_n = [[None for _ in range(5)] for _ in range(5)]
        self.grid_w_su = [[None for _ in range(5)] for _ in range(5)]
        self.grid_w_p = [[None for _ in range(5)] for _ in range(5)]
        self.grid_w_wi = [[None for _ in range(5)] for _ in range(5)]
        self.grid_w_a = [[None for _ in range(5)] for _ in range(5)]
                
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_w_s, len(self.grid_w_s), len(self.grid_w_s[0]), lbl.women_labels, lbl.shirt_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=2, padx=10, pady=5)
        self.create_grid(frame,self.grid_w_n, len(self.grid_w_n), len(self.grid_w_n[0]), lbl.women_labels, lbl.name_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=3, padx=10, pady=5)
        self.create_grid(frame,self.grid_w_su, len(self.grid_w_su), len(self.grid_w_su[0]), lbl.women_labels, lbl.surname_labels)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=2, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_w_p, len(self.grid_w_p), len(self.grid_w_p[0]), lbl.women_labels, lbl.pasta_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=2, column=2, padx=10, pady=5)
        self.create_grid(frame,self.grid_w_wi, len(self.grid_w_wi), len(self.grid_w_wi[0]), lbl.women_labels, lbl.wine_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=2, column=3, padx=10, pady=5)
        self.create_grid(frame,self.grid_w_a, len(self.grid_w_a), len(self.grid_w_a[0]), lbl.women_labels, lbl.age_labels)
        
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=3, column=3, padx=10, pady=5)
        button = tk.Button(frame, text="Solve", width=2, height=1, command=self.solve_click)
        button.grid(row=0, column=0)

    def create_frame(self, frame):
        for i in range(3):
            for j in range(1):
                frame.grid(row=i, column=j, padx=5, pady=5)

    def create_grid(self, frame, grid, row, column, row_labels, column_labels):
        custom_font = font.Font(size=6)
        for i in range(len(column_labels)):
            label = tk.Label(frame, text=column_labels[i], borderwidth=1, relief="solid", width=14, height=2, font=custom_font)
            label.grid(row=0, column=i+1)
        for i in range(len(row_labels)):
            label = tk.Label(frame, text=row_labels[i], borderwidth=1, relief="solid", width=14, height=2, font=custom_font)
            label.grid(row=i+1, column=0)
        for i in range(row):
            for j in range(column):
                button = tk.Button(frame, text="", width=2, height=1, command=lambda grid=grid, row=i, col=j: self.on_button_click(grid,row, col))
                button.grid(row=i+1, column=j+1)
                grid[i][j] = button

    def solve_click(self):
        self.controller.solve()
        

    def on_button_click(self, grid, row, col):
        button = grid[row][col]
        current_text = button.cget("text")
        name = self.get_grid_name(grid)
        check = False
        if name=="P1" or name=="P2" or name == "P3" or name == "P4" or name == "P5" or name == "P6":
            check = True
        if current_text == "":
            '''
            for i in range(len(grid)):
                grid[i][col].config(text="X")
            for i in range(len(grid[0])):
                grid[row][i].config(text="X")
            '''
            button.config(text="O")
            if(check == True):
                self.controller.add_constraint("constraint "+name+"[" + str(row)+","+str(col)+"] == true;")
        else:
            if current_text == "O":
                button.config(text="X")
                if(check == True):
                    self.controller.replace_constraint("constraint "+name+"[" + str(row)+","+str(col)+"] == true;", "constraint "+self.get_grid_name(grid)+"[" + str(row)+","+str(col)+"] == false;")
            else:
                button.config(text="")
                if(check == True):
                    self.controller.remove_constraint("constraint "+name+"[" + str(row)+","+str(col)+"] == false;")


    def display_data(self,data):
        print(f"Affichage des données : {data}")

    def get_grid_name(self,grid):
        if(grid == self.grid_w_s):
            return "P1"
        else:
            if(grid == self.grid_w_n):
                return "P2"
            else:
                if(grid == self.grid_w_su) :
                    return "P3"
                else:
                    if(grid == self.grid_w_p) :
                        return "P4"
                    else:
                        if(grid == self.grid_w_wi) :
                            return "P5"
                        else:
                            if(grid == self.grid_w_a) :
                                return "P6"
        return ""
    


