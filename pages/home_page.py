import tkinter as tk
import tkinter.ttk as ttk
from function import Request


class HomePage(tk.Frame):
    """Class representing the Home Page of the application."""

    def __init__(self, parent, callback):
        """Initialize the Home Page.

        Args:
            parent (tk.Widget): The parent widget.
            callback (callable): The callback function to be called when the Konami code is entered.
        """
        super().__init__(parent)
        self.callback = callback

        # Register the Konami code sequence

        self.configure(bg="")

        map_rotation_text = checkMapRotation()  # Get the map rotation text
        predator_text = checkPredator()  # Get the predator text

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

        self.mapLabel = ttk.Label(
            self, text=map_rotation_text, style="Map.TLabel", justify="center")
        self.mapLabel.pack(padx=10, pady=10, fill="both")

        self.predLabel = ttk.Label(
            self, text=predator_text, style="Pred.TLabel", justify="center")
        self.predLabel.pack(padx=10, pady=(0, 10), fill="both")

        self.update_labels()  # Update the labels with the latest data

    def update_labels(self):
        """Update the labels with the latest data."""
        map_rotation_text = checkMapRotation()  # Get the map rotation text
        predator_text = checkPredator()  # Get the predator text

        # Update the map label text
        self.mapLabel.config(text=map_rotation_text)
        # Update the predator label text
        self.predLabel.config(text=predator_text)

        # Schedule next update after 1 minute
        self.after(60000, self.update_labels)


def checkMapRotation():
    """Retrieve the map rotation information from the API and format the text."""
    data = Request(
        "https://api.mozambiquehe.re/maprotation?version=2", "").json()
    Pub_current_map = data['battle_royale']['current']['map']
    Pub_current_map_remainingTime = data['battle_royale']['current']['remainingTimer']
    Pub_next_map = data['battle_royale']['next']['map']

    ranked_current_map = data['ranked']['current']['map']
    ranked_current_map_remainingTime = data['ranked']['current']['remainingTimer']
    ranked_next_map = data['ranked']['next']['map']

    return f"The current casual map is {Pub_current_map}. Time remaining: {Pub_current_map_remainingTime}. Next map: {Pub_next_map}.\n\nThe current ranked map is {ranked_current_map}. Time remaining: {ranked_current_map_remainingTime}. Next map: {ranked_next_map}."


def checkPredator():
    """Retrieve the predator cap information from the API and format the text."""
    data = Request("https://api.mozambiquehe.re/predator", "").json()
    pc_Cap = data["RP"]['PC']["val"]
    xbox_Cap = data["RP"]['X1']["val"]
    ps_Cap = data["RP"]['PS4']["val"]
    switch_Cap = data["RP"]['SWITCH']["val"]

    return f"The current predator cap on PC is {formatNumber(pc_Cap)} RP.\n\nThe current predator cap on XBOX is {formatNumber(xbox_Cap)} RP.\n\nThe current predator cap on PLAYSTATION is {formatNumber(ps_Cap)} RP.\n\nThe current predator cap on SWITCH is {formatNumber(switch_Cap)} RP."


def formatNumber(NUMBER):
    """Format the given number with comma as a thousands separator and no decimal places."""
    return "{:,.0f}".format(NUMBER)