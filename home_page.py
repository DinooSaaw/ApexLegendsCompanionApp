import tkinter as tk
import keyboard

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Home Page")
        label.pack()

        # Register the Konami code sequence
        expected_sequence = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]
        self.current_index = 0

        def check_sequence(event):
            if self.focus_get() is None:  # Check if application is not in focus
                return print("Lost of focus")
            
            print(event.name)
            
            if event.name == expected_sequence[self.current_index]:
                self.current_index += 1
                if self.current_index == len(expected_sequence):
                    print("Konami code entered!")
                    self.current_index = 0
                    keyboard.unhook_all()
            else:
                self.current_index = 0

        keyboard.on_press(check_sequence)
