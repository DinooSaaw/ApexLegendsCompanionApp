import tkinter as tk

class StatsPage(tk.Frame):
    """Class representing the Stats Page of the application."""

    def __init__(self, parent):
        """Initialize the Stats Page.

        Args:
            parent (tk.Widget): The parent widget.
        """
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Stats Page")
        label.pack()