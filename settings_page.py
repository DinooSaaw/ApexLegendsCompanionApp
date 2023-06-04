import tkinter as tk

class SettingsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Settings Page")
        label.pack()
