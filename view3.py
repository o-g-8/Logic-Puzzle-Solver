import tkinter as tk
from tkinter import font
from observer import Observer
from controller3 import Controller

import labels3 as lbl

class View(Observer):
    def __init__(self, args, controller, observable, root):
        self.args = args
        self.n_clue = 0
        self.controller = controller
        self.puzzle = observable
        self.puzzle.add_observer(self)

        self.root = root
        self.root.title("Puzzle 3")
    
        self.clue_frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        self.clue_frame.grid(row=4, column=3, padx=10, pady=5)

        self.n_person: 3
        self.n_object: 3
        self.n_place: 3

        self.grid_p_o = [[None for _ in range(3)] for _ in range(3)]
        self.grid_p_pl = [[None for _ in range(3)] for _ in range(3)]


        self.grid_o_pl = [[None for _ in range(3)] for _ in range(3)]

        lbl.rename()
                
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_p_o, len(self.grid_p_o), len(self.grid_p_o[0]), lbl.person_labels, lbl.object_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=2, padx=10, pady=5)
        self.create_grid(frame,self.grid_p_pl, len(self.grid_p_pl), len(self.grid_p_pl[0]), lbl.person_labels, lbl.place_labels)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=2, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_o_pl, len(self.grid_o_pl), len(self.grid_o_pl[0]), lbl.place_labels, lbl.object_labels)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=3, column=2, padx=10, pady=5)
        button = tk.Button(frame, text="Solve", width=2, height=1, command=self.solve_click)
        button.grid(row=0, column=0)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=4, column=1, padx=10, pady=5)
        button = tk.Button(frame, text="Add Constraints", width=10, height=1, command=self.add_constraint_click)
        button.grid(row=0, column=0)

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

    def add_constraint_click(self):
        self.controller.add_clue()
        
    def on_button_click(self, grid, row, col):
        button = grid[row][col]
        current_text = button.cget("text")
        name = self.get_grid_name(grid)
        check = False
        if name=="P1" or name=="P2":
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
        if(grid == self.grid_p_o):
            return "P1"
        else:
            if(grid == self.grid_p_pl):
                return "P2"
        return ""
    
    def reset_button(self):
        for i in self.grid_o_pl:
            for j in i:
                j.config(text="")
        for i in self.grid_p_o:
            for j in i:
                j.config(text="")
        for i in self.grid_p_pl:
            for j in i:
                j.config(text="")
    
    def update(self,text):
        custom_font = font.Font(size=6)
        label = tk.Label(self.clue_frame, text=text, wraplength=200, justify="left", font=custom_font)
        label.grid(row=self.n_clue, column=0)
        self.n_clue += 1
        self.reset_button()
        
    


