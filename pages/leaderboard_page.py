import tkinter as tk
from tkinter import ttk
from function import Request


class LeaderboardPage(tk.Frame):
    """Class representing the Leaderboard Page of the application."""

    def __init__(self, parent):
        """Initialize the Leaderboard Page.

        Args:
            parent (tk.Widget): The parent widget.
        """
        super().__init__(parent)

        # Create a Treeview widget to display leaderboard data
        self.treeview = ttk.Treeview(self)
        self.treeview.pack(fill="both", expand=True)

        # Configure the Treeview columns
        self.treeview["columns"] = ("Rank", "Player", "Score")
        self.treeview.heading("#0", text="Legend")
        self.treeview.heading("Rank", text="Rank")
        self.treeview.heading("Player", text="Player")
        self.treeview.heading("Score", text="Score")

        # Retrieve leaderboard data from the API
        data = Request(
            "https://api.mozambiquehe.re/leaderboard?legend=Global", "").json()

        if "Error" in data:
            # Display API error message
            self.treeview.insert("", "end", text="Error",
                                 values=(data["Error"], "", ""))
        else:
            # Display leaderboard data
            leaderboard = data.get("global", [])
            for player in leaderboard:
                rank = player.get("rank", "")
                name = player.get("name", "")
                score = player.get("score", "")
                self.treeview.insert("", "end", text="",
                                     values=(rank, name, score))
