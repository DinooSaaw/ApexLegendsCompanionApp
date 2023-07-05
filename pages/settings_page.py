import tkinter as tk
from pymongo import MongoClient
from database import update_document, find_documents, connect_to_mongodb

class SettingsPage(tk.Frame):
    """Class representing the Settings Page of the application."""

    def __init__(self, parent):
        """Initialize the Settings Page.

        Args:
            parent (tk.Widget): The parent widget.
        """
        super().__init__(parent)
        client = connect_to_mongodb()
        db = client["ALC"]
        collection = db["Settings"]
        settings_data = find_documents(collection, {"_id": "Settings"})
        self.settings_document = settings_data.next()
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface."""
        if self.settings_document:
            # Create BooleanVar variables for each setting
            display_stats_var = tk.BooleanVar(value=self.settings_document["displayStats"])
            display_home_var = tk.BooleanVar(value=self.settings_document["displayHome"])
            display_leaderboard_var = tk.BooleanVar(value=self.settings_document["displayLeaderboard"])
            konami_code_var = tk.BooleanVar(value=self.settings_document["konamiCode"])

            # Create switches and entry
            stats_switch = tk.Checkbutton(self, text="Display Stats", variable=display_stats_var)
            stats_switch.pack()
            
            home_switch = tk.Checkbutton(self, text="Display Home", variable=display_home_var)
            home_switch.pack()

            leaderboard_switch = tk.Checkbutton(self, text="Display Leaderboard", variable=display_leaderboard_var)
            leaderboard_switch.pack()

            leaderboard_amount_label = tk.Label(self, text="Leaderboard Amount:")
            leaderboard_amount_label.pack()

            leaderboard_amount_entry = tk.Entry(self)
            leaderboard_amount_entry.pack()
            leaderboard_amount_entry.insert(0, str(self.settings_document["displayLeaderboardAmount"]))

            konami_switch = tk.Checkbutton(self, text="Konami Code", variable=konami_code_var)
            konami_switch.pack()

    def save_settings(self):
        """Save the settings."""
        if self.settings_document:
            # Retrieve the settings values
            display_stats = display_stats_var.get()
            display_home = display_home_var.get()
            display_leaderboard = display_leaderboard_var.get()
            leaderboard_amount = int(leaderboard_amount_entry.get())
            konami_code = konami_code_var.get()

            # Process the settings data as needed (e.g., save to a file or apply to the application)

            # For demonstration purposes, print the settings values
            print("Settings Saved:")
            print("Display Stats:", display_stats)
            print("Display Home:", display_home)
            print("Display Leaderboard:", display_leaderboard)
            print("Leaderboard Amount:", leaderboard_amount)
            print("Konami Code:", konami_code)
        else:
            print("No settings document found.")
