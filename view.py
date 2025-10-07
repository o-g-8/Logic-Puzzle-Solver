import tkinter as tk
from tkinter import font
from observer import Observer
from controller import Controller

import labels as lbl

class View(Observer):
    def __init__(self, args, controller, observable, root):
        
        self.controller = controller
        self.puzzle = observable
        self.puzzle.add_observer(self)

        self.root = root
        self.root.title("Puzzle")
    

        self.n_actor: int = args.actor
        self.n_film: int = args.film
        self.n_day: int = args.day
        self.n_time: int = args.time

        self.grid_a_f = [[None for _ in range(args.film)] for _ in range(args.actor)]
        self.grid_a_d = [[None for _ in range(args.day)] for _ in range(args.actor)]
        self.grid_a_t = [[None for _ in range(args.time)] for _ in range(args.actor)]

        self.grid_t_f = [[None for _ in range(args.film)] for _ in range(args.time)]
        self.grid_d_f = [[None for _ in range(args.film)] for _ in range(args.day)]

        self.grid_t_d = [[None for _ in range(args.day)] for _ in range(args.time)]
                
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_a_f, len(self.grid_a_f), len(self.grid_a_f[0]), lbl.actor_labels, lbl.film_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=2, padx=10, pady=5)
        self.create_grid(frame,self.grid_a_d, len(self.grid_a_d), len(self.grid_a_d[0]), lbl.actor_labels, lbl.day_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=3, padx=10, pady=5)
        self.create_grid(frame,self.grid_a_t, len(self.grid_a_t), len(self.grid_a_t[0]), lbl.actor_labels, lbl.time_labels)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=2, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_t_f, len(self.grid_t_f), len(self.grid_t_f[0]), lbl.time_labels, lbl.film_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=2, column=2, padx=10, pady=5)
        self.create_grid(frame,self.grid_d_f, len(self.grid_d_f), len(self.grid_d_f[0]), lbl.day_labels, lbl.film_labels)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=3, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_t_d, len(self.grid_t_d), len(self.grid_t_d[0]), lbl.time_labels, lbl.day_labels)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=4, column=1, padx=10, pady=5)
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
        if name=="P1" or name=="P2" or name == "P3":
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
        if(grid == self.grid_a_f):
            return "P1"
        else:
            if(grid == self.grid_a_d):
                return "P2"
            else:
                if(grid == self.grid_a_t) :
                    return "P3"
        return ""
    


