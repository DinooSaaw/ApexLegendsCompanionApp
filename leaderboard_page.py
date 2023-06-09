import tkinter as tk

class LeaderboardPage(tk.Frame):
    """Class representing the Leaderboard Page of the application."""

    def __init__(self, parent):
        """Initialize the Leaderboard Page.

        Args:
            parent (tk.Widget): The parent widget.
        """
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Leaderboard Page")
        label.pack()
