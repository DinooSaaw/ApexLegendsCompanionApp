import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Home Page")
        label.pack()
