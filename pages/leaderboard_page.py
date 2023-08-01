import tkinter as tk
from tkinter import ttk


def get_score_color(score):
    score = int(score.replace(",", ""))
    if score >= 100000:
        return "red"
    elif score >= 21000:
        return "purple"
    elif score >= 17000:
        return "blue"
    elif score >= 13000:
        return "light blue"
    elif score >= 9000:
        return "gold"
    elif score >= 5000:
        return "gray"
    elif score >= 0:
        return "brown"
    else:
        return "black"  # Default color for scores below 400K


class LeaderboardPage(tk.Frame):
    """Class representing the Leaderboard Page of the application."""

    def __init__(self, parent):
        """Initialize the Leaderboard Page.

        Args:
            parent (tk.Widget): The parent widget.
        """
        super().__init__(parent)

        # Create a Treeview widget to display leaderboard data
        self.treeview = ttk.Treeview(self, show="headings")
        self.treeview.pack(fill="both", expand=True)

        # Configure the Treeview columns in the desired order (Rank, Player Name, Score)
        self.treeview["columns"] = ("Rank", "Player", "Score")
        self.treeview.column("Rank", width=70, anchor="center")  # Adjust the width of the Rank column
        self.treeview.heading("Rank", text="Rank")
        self.treeview.column("Player", anchor="center")  # Center the text in the "Player" column
        self.treeview.heading("Player", text="Player Name")
        self.treeview.column("Score", anchor="center")  # Center the text in the "Score" column
        self.treeview.heading("Score", text="LP")

        # Dummy leaderboard data
        dummy_data = [
            {"rank": 1, "name": "LG_WeThePeople1", "score": "591,758"},
            {"rank": 2, "name": "FB-AkesGaming", "score": "586,504"},
            {"rank": 3, "name": "MtF Ruhhnq", "score": "526,344"},
            {"rank": 4, "name": "darekimiwfanboy", "score": "521,237"},
            {"rank": 5, "name": "Need A Soda", "score": "518,775"},
            {"rank": 6, "name": "Kitty", "score": "514,189"},
            {"rank": 7, "name": "SOUVENIR", "score": "481,943"},
            {"rank": 8, "name": "neo_zaurusu", "score": "481,205"},
            {"rank": 9, "name": "RatzN33dLuv2", "score": "472,895"},
            {"rank": 10, "name": "PapiMRVN", "score": "462,642"},
            {"rank": 11, "name": "Player11", "score": "97,642"},
            {"rank": 12, "name": "Player12", "score": "62,602"},
            {"rank": 13, "name": "Player13", "score": "42,742"},
            {"rank": 14, "name": "Player14", "score": "32,792"},
            {"rank": 15, "name": "Player15", "score": "21,000"},
            {"rank": 16, "name": "Player16", "score": "18,000"},
            {"rank": 17, "name": "Player17", "score": "15,000"},
            {"rank": 18, "name": "Player18", "score": "11,000"},
            {"rank": 19, "name": "Player19", "score": "5,200"},
            {"rank": 20, "name": "Player20", "score": "800"},
        ]

        # Display leaderboard data
        for player in dummy_data:
            rank = player["rank"]
            name = player["name"]
            score = player["score"]
            score_color = get_score_color(score)
            self.treeview.insert("", "end", values=(rank, name, score))

            # Apply the color tag to each cell in the "Score" column
            self.treeview.tag_configure(score_color, foreground=score_color)
            self.treeview.item(self.treeview.get_children()[-1], tags=(score_color,))
