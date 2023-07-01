import tkinter as tk
from function import Request  # Import the Request function from the function module
import keyboard


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
        expected_sequence = ["up", "up", "down", "down",
                             "left", "right", "left", "right", "b", "a"]
        self.current_index = 0

        def check_sequence(event):
            """Check if the entered key sequence matches the Konami code.

            Args:
                event (keyboard.KeyboardEvent): The keyboard event representing the pressed key.
            """
            if self.focus_get() is None:  # Check if application is not in focus
                return

            print(event.name)
            if event.name == expected_sequence[self.current_index].lower():
                self.current_index += 1
                if self.current_index == len(expected_sequence):
                    print("Konami code entered!")
                    self.current_index = 0
                    self.callback()  # Call the callback function in Application
                    keyboard.unhook_all()
            else:
                self.current_index = 0

        # Create the gray box with template text
        self.box = tk.Frame(self, bg="gray", width=200, height=100)
        self.box.pack(pady=10)

        self.mapLabel = tk.Label(self.box, fg="white", bg="gray")
        self.mapLabel.pack()

        self.box2 = tk.Frame(self, bg="gray", width=200, height=100)
        self.box2.pack(pady=10)
        self.predLabel = tk.Label(self.box2, fg="white", bg="gray")
        self.predLabel.pack()

        keyboard.on_press(check_sequence)
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

    return f"The current casual map is {Pub_current_map}. Time remaining: {Pub_current_map_remainingTime}. Next map: {Pub_next_map}. \nThe current ranked map is {ranked_current_map}. Time remaining: {ranked_current_map_remainingTime}. Next map: {ranked_next_map}."


def checkPredator():
    """Retrieve the predator cap information from the API and format the text."""
    data = Request("https://api.mozambiquehe.re/predator", "").json()
    pc_Cap = data["RP"]['PC']["val"]
    xbox_Cap = data["RP"]['X1']["val"]
    ps_Cap = data["RP"]['PS4']["val"]
    switch_Cap = data["RP"]['SWITCH']["val"]

    return f"The current predator cap on PC is {formatNumber(pc_Cap)} RP.\nThe current predator cap on XBOX is {formatNumber(xbox_Cap)} RP.\nThe current predator cap on PLAYSTATION is {formatNumber(ps_Cap)} RP.\nThe current predator cap on SWITCH is {formatNumber(switch_Cap)} RP."


def formatNumber(NUMBER):
    """Format the given number with comma as a thousands separator and no decimal places."""
    return "{:,.0f}".format(NUMBER)