import tkinter as tk

class LeaderboardPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Leaderboard Page")
        label.pack()
