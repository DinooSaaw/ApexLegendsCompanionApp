import tkinter as tk
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
        label = tk.Label(self, text="Welcome to the Home Page")
        label.pack()

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
        label1 = tk.Label(box1, text="Template Text 1", fg="white", bg="gray")
        label1.pack()

        box2 = tk.Frame(self, bg="gray", width=200, height=100)
        box2.pack(pady=10)
        label2 = tk.Label(box2, text="Template Text 2", fg="white", bg="gray")
        label2.pack()
        
        keyboard.on_press(check_sequence) 