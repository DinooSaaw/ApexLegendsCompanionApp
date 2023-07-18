import tkinter as tk
from tkinter import ttk
from function import Request


class StatsPage(tk.Frame):
    """Page that displays statistics."""

    def __init__(self, parent):
        """Initialize the StatsPage class.

        Args:
            parent: The parent widget.
        """
        super().__init__(parent)

        # Player Name Entry
        player_name_label = tk.Label(self, text="Player Name:")
        player_name_label.grid(row=1, column=0)
        self.player_name_entry = tk.Entry(self)
        self.player_name_entry.grid(row=1, column=1)

        # Platform Dropdown
        platform_label = tk.Label(self, text="Platform:")
        platform_label.grid(row=2, column=0)

        self.platform_var = tk.StringVar(self)
        self.platform_dropdown = ttk.Combobox(
            self, textvariable=self.platform_var)
        self.platform_dropdown["values"] = (
            "X1", "PS4", "PC", "SWITCH")  # Add your platform options here
        self.platform_dropdown.grid(row=2, column=1)

        # Search Button
        search_button = tk.Button(self, text="Search", command=self.search)
        search_button.grid(row=3, column=0, columnspan=2)

        # Level Label
        self.level_label = tk.Label(self, text="")
        self.level_label.grid(row=4, column=0, sticky='w')

        # Create a frame for data labels
        self.data_frame = ttk.Frame(self)
        self.data_frame.grid(row=5, column=0, columnspan=2, sticky="w")

    def search(self):
        """Search button callback function."""
        player_name = self.player_name_entry.get().strip()
        platform = self.platform_var.get()

        if not player_name:
            self.display_error_message("Please enter a player name.")
            return

        if not platform:
            self.display_error_message("Please select a platform.")
            return

        # Perform search operation with player_name and platform values
        data = Request(
            f"https://api.mozambiquehe.re/bridge?&player={player_name}&platform={platform}", "").json()

        if 'Error' in data:
            return self.display_error_message(data['Error'])

        self.display_data_labels(data)

    def display_error_message(self, error_message):
        """Display error message label."""
        self.clear_data_labels()

        error_label = tk.Label(
            self.data_frame, text=f"Error: {error_message}", fg="red")
        error_label.grid(row=0, column=0, sticky='w')
        self.data_frame.grid_columnconfigure(0, weight=1)

    def clear_data_labels(self):
        """Clear previous data labels if any."""
        for widget in self.data_frame.winfo_children():
            widget.destroy()

    def display_data_labels(self, data):
        """Display the data labels with the retrieved data."""
        self.clear_data_labels()

        name = data["global"]["name"]
        platform = data["global"]["platform"]
        level = data["global"]["level"]
        rank_score = data["global"]["rank"]["rankScore"]
        rank_name = data["global"]["rank"]["rankName"]
        legend_name = data["legends"]["selected"]["LegendName"]
        legend_data = data["legends"]["selected"]["data"]

        self.level_label.config(text=f"Level: {level}")

        # Add labels for the data
        self.create_data_label(f"Name: {name}", 0)
        self.create_data_label(f"Platform: {platform}", 1)
        self.create_data_label(
            f"Rank Name: {rank_name}", 2, fg=self.get_rank_name_color(rank_name))
        self.create_data_label(f"LP: {formatNumber(rank_score)}", 3)
        self.create_data_label(f"Legend Name: {legend_name}", 4)

        for i, tracker in enumerate(legend_data[:3]):
            tracker_name = tracker["name"]
            tracker_value = tracker["value"]
            self.create_data_label(f"{tracker_name}: {tracker_value}", i + 5)

    def create_data_label(self, text, row, fg="black"):
        """Create a data label with the given text and grid position."""
        label = tk.Label(self.data_frame, text=text, fg=fg)
        label.grid(row=row, column=0, sticky='w')
        self.data_frame.grid_columnconfigure(0, weight=1)
        return label

    @staticmethod
    def get_rank_name_color(rank_name):
        """Get the color for the rank name label based on the rank name value."""
        rank_name_colors = {
            "Bronze": "brown",
            "Silver": "gray",
            "Gold": "gold",
            "Platinum": "light blue",
            "Diamond": "blue",
            "Master": "purple",
            "Apex Predator": "red"
        }
        return rank_name_colors.get(rank_name, "black")


def formatNumber(number):
    """Format the given number with comma as a thousands separator and no decimal places."""
    return "{:,.0f}".format(number)
