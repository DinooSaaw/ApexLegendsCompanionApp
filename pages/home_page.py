import tkinter as tk
import tkinter.ttk as ttk
from function import Request


class HomePage(tk.Frame):
    """Class representing the Home Page of the application."""

    def __init__(self, parent):
        """Initialize the Home Page.

        Args:
            parent (tk.Widget): The parent widget.
        """
        super().__init__(parent)

        self.configure(bg="")

        style = ttk.Style()
        style.configure(
            "Map.TLabel",
            background="light grey",
            relief="dashed",
            borderwidth=1,
            padding=10
        )

        style.configure(
            "Pred.TLabel",
            background="light grey",
            relief="dashed",
            borderwidth=1,
            padding=10
        )

        self.map_label = ttk.Label(
            self, style="Map.TLabel", justify="center")
        self.map_label.pack(padx=10, pady=10, fill="both")

        self.pred_label = ttk.Label(
            self, style="Pred.TLabel", justify="center")
        self.pred_label.pack(padx=10, pady=(0, 10), fill="both")

        self.update_labels()  # Update the labels with the latest data

    def update_labels(self):
        """Update the labels with the latest data."""
        map_rotation_text = check_map_rotation()  # Get the map rotation text
        predator_text = check_predator()  # Get the predator text

        # Update the map label text
        self.map_label.config(text=map_rotation_text)
        # Update the predator label text
        self.pred_label.config(text=predator_text)

        # Schedule next update after 1 minute
        self.after(60000, self.update_labels)


def check_map_rotation():
    """Retrieve the map rotation information from the API and format the text."""
    try:
        data = Request(
            "https://api.mozambiquehe.re/maprotation?version=2", "").json()
        pub_current_map = data['battle_royale']['current']['map']
        pub_current_map_remaining_time = data['battle_royale']['current']['remainingTimer']
        pub_next_map = data['battle_royale']['next']['map']

        ranked_current_map = data['ranked']['current']['map']
        ranked_current_map_remaining_time = data['ranked']['current']['remainingTimer']
        ranked_next_map = data['ranked']['next']['map']

        return f"The current casual map is {pub_current_map}. Time remaining: {pub_current_map_remaining_time}. Next map: {pub_next_map}.\n\nThe current ranked map is {ranked_current_map}. Time remaining: {ranked_current_map_remaining_time}. Next map: {ranked_next_map}."
    except Exception as e:
        # Handle API request errors
        print(f"Error retrieving map rotation: {e}")
        return "Error retrieving map rotation."


def check_predator():
    """Retrieve the predator cap information from the API and format the text."""
    try:
        data = Request("https://api.mozambiquehe.re/predator", "").json()
        pc_cap = data["RP"]['PC']["val"]
        xbox_cap = data["RP"]['X1']["val"]
        ps_cap = data["RP"]['PS4']["val"]
        switch_cap = data["RP"]['SWITCH']["val"]

        return f"The current predator cap on PC is {format_number(pc_cap)} RP.\n\nThe current predator cap on XBOX is {format_number(xbox_cap)} RP.\n\nThe current predator cap on PLAYSTATION is {format_number(ps_cap)} RP.\n\nThe current predator cap on SWITCH is {format_number(switch_cap)} RP."
    except Exception as e:
        # Handle API request errors
        print(f"Error retrieving predator cap: {e}")
        return "Error retrieving predator cap."


def format_number(number):
    """Format the given number with comma as a thousands separator and no decimal places."""
    return "{:,.0f}".format(number)
