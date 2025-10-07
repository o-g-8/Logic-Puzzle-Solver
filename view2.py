import tkinter as tk
from tkinter import font
from observer import Observer
from controller2 import Controller

import labels2 as lbl

class View(Observer):
    def __init__(self, args, controller, observable, root):
        
        self.controller = controller
        self.puzzle = observable
        self.puzzle.add_observer(self)

        self.root = root
        self.root.title("Puzzle 2")
    

        self.n_monitor: int = args.monitor
        self.n_processor: int = args.processor
        self.n_harddisk: int = args.harddisk
        self.n_price: int = args.price

        self.grid_m_p = [[None for _ in range(args.processor)] for _ in range(args.monitor)]
        self.grid_m_h = [[None for _ in range(args.harddisk)] for _ in range(args.monitor)]
        self.grid_m_pri = [[None for _ in range(args.price)] for _ in range(args.monitor)]

        self.grid_t_f = [[None for _ in range(args.processor)] for _ in range(args.price)]
        self.grid_d_f = [[None for _ in range(args.processor)] for _ in range(args.harddisk)]

        self.grid_t_d = [[None for _ in range(args.harddisk)] for _ in range(args.price)]
                
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_m_p, len(self.grid_m_p), len(self.grid_m_p[0]), lbl.monitor_labels, lbl.processor_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=2, padx=10, pady=5)
        self.create_grid(frame,self.grid_m_h, len(self.grid_m_h), len(self.grid_m_h[0]), lbl.monitor_labels, lbl.harddisk_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=1, column=3, padx=10, pady=5)
        self.create_grid(frame,self.grid_m_pri, len(self.grid_m_pri), len(self.grid_m_pri[0]), lbl.monitor_labels, lbl.price_labels)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=2, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_t_f, len(self.grid_t_f), len(self.grid_t_f[0]), lbl.price_labels, lbl.processor_labels)
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=2, column=2, padx=10, pady=5)
        self.create_grid(frame,self.grid_d_f, len(self.grid_d_f), len(self.grid_d_f[0]), lbl.harddisk_labels, lbl.processor_labels)

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.grid(row=3, column=1, padx=10, pady=5)
        self.create_grid(frame,self.grid_t_d, len(self.grid_t_d), len(self.grid_t_d[0]), lbl.price_labels, lbl.harddisk_labels)

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
        if(grid == self.grid_m_p):
            return "P1"
        else:
            if(grid == self.grid_m_h):
                return "P2"
            else:
                if(grid == self.grid_m_pri) :
                    return "P3"
        return ""
    


