import tkinter as tk
from function import Request
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
        expected_sequence = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]
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


        # Create the gray boxes with template text
        box1 = tk.Frame(self, bg="gray", width=200, height=100)
        box1.pack(pady=10)
        
        mapLabel = tk.Label(box1, text=checkMapRotation(), fg="white", bg="gray")
        mapLabel.pack()

        box2 = tk.Frame(self, bg="gray", width=200, height=100)
        box2.pack(pady=10)
        predLabel = tk.Label(box2, text=checkPredator(), fg="white", bg="gray")
        predLabel.pack()
        
        keyboard.on_press(check_sequence)

def checkMapRotation():
    data = Request("https://api.mozambiquehe.re/maprotation?version=2", "").json()
    Pub_current_map = data['battle_royale']['current']['map']
    Pub_current_map_remainingTime = data['battle_royale']['current']['remainingTimer']
    Pub_next_map = data['battle_royale']['next']['map']

    ranked_current_map = data['ranked']['current']['map']
    ranked_current_map_remainingTime = data['ranked']['current']['remainingTimer']
    ranked_next_map = data['ranked']['next']['map']
    return f"The current casual map is {Pub_current_map}. Time remaining: {Pub_current_map_remainingTime}. Next map: {Pub_next_map}. \n The current ranked map is {ranked_current_map}. Time remaining: {ranked_current_map_remainingTime}. Next map: {ranked_next_map}."

def checkPredator():
    data = Request("https://api.mozambiquehe.re/predator", "").json()
    pc_Cap = data["RP"]['PC']["val"]
    xbox_Cap = data["RP"]['X1']["val"]
    ps_Cap = data["RP"]['PS4']["val"]
    switch_Cap = data["RP"]['SWITCH']["val"]
    
    return f"The current predator cap on PC is {pc_Cap}RP.\n The current predator cap on XBOX is {xbox_Cap}RP.\n The current predator cap on PLAYSTAION is {ps_Cap}RP.\n The current predator cap on SWITCH is {switch_Cap}RP."