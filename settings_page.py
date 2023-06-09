import tkinter as tk

class SettingsPage(tk.Frame):
    """Class representing the Settings Page of the application."""

    def __init__(self, parent):
        """Initialize the Settings Page.

        Args:
            parent (tk.Widget): The parent widget.
        """
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Settings Page")
        label.pack()
