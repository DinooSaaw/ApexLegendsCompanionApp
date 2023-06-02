import tkinter as tk

class StatsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Stats Page")
        label.pack()
