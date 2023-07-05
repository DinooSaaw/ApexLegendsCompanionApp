import tkinter as tk
from function import Request

class LeaderboardPage(tk.Frame):
    """Class representing the Leaderboard Page of the application."""

    def __init__(self, parent):
        """Initialize the Leaderboard Page.

        Args:
            parent (tk.Widget): The parent widget.
        """
        super().__init__(parent)
        data = Request("https://api.mozambiquehe.re/leaderboard?legend=Global", "").json()

        label = tk.Label(self, text=data["Error"])
        label.pack()
