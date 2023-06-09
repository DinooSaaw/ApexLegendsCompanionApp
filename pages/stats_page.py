import tkinter as tk
from tkinter import ttk
from function import Request


class StatsPage(tk.Frame):
    """Page that displays statistics."""

    def __init__(self, parent, login_callback, username):
        """Initialize the StatsPage class.

        Args:
            parent: The parent widget.
            login_callback: The callback function for login.
            username: The username of the logged-in user.

        """
        super().__init__(parent)
        self.login_callback = login_callback
        self.username = username

        # Player Name Entry
        player_name_label = tk.Label(self, text="Player Name:")
        player_name_label.grid(row=1, column=0)
        self.player_name_entry = tk.Entry(self)
        self.player_name_entry.grid(row=1, column=1)
        self.player_name_entry.insert( 0, username)

        # Platform Dropdown
        platform_label = tk.Label(self, text="Platform:")
        platform_label.grid(row=2, column=0)

        self.platform_var = tk.StringVar(self)
        self.platform_dropdown = ttk.Combobox(
            self, textvariable=self.platform_var)
        self.platform_dropdown["values"] = (
            "XBOX", "PS", "PC")  # Add your platform options here
        self.platform_dropdown.grid(row=2, column=1)

        # Search Button
        search_button = tk.Button(self, text="Search", command=self.search)
        search_button.grid(row=3, column=0, columnspan=2)

        # Level Label
        self.level_label = tk.Label(self, text="")
        self.level_label.grid(row=4, column=0, sticky='w')

        # Create labels for displaying data
        self.labels = []

    def get_player_name(self):
        """Get the value entered in the player name entry field."""
        return self.player_name_entry.get()

    def get_selected_platform(self):
        """Get the selected value from the platform dropdown."""
        platform = self.platform_var.get()
        if platform == "XBOX":
            return "X1"
        elif platform == "PC":
            return "PC"
        elif platform == "PS":
            return "PS4"

    def search(self):
        """Search button callback function."""
        player_name = self.get_player_name()
        platform = self.get_selected_platform()
        # Perform search operation with player_name and platform values
        data = Request(
            f"https://api.mozambiquehe.re/bridge?&player={player_name}&platform={platform}", "").json()

        if 'Error' in data:
            return self.display_error_message(data)

        # Clear previous data labels if any
        self.clear_labels()

        self.update_data_labels(data)

    def display_error_message(self, data):
        """Display error message label."""
        error_message = data['Error']
        if hasattr(self, 'error_label'):
            self.error_label.destroy()
        # Display error message or handle it as desired
        self.error_label = tk.Label(
            self, text=f"Error: {error_message}", fg="red")
        self.error_label.grid(row=5, column=0, columnspan=2)

        # Clear previous data labels if any
        self.clear_labels()

    def clear_labels(self):
        """Clear previous data labels if any."""
        for label in self.labels:
            label.destroy()
        self.labels = []

    def update_data_labels(self, data):
        """Update the data labels with the retrieved data."""
        name = data["global"]["name"]
        platform = data["global"]["platform"]
        level = data["global"]["level"]
        rankScore = data["global"]["rank"]["rankScore"]
        rankName = data["global"]["rank"]["rankName"]
        LegendName = data["legends"]["selected"]["LegendName"]
        LegendData = data["legends"]["selected"]["data"]

        # Add labels for the data
        self.labels.append(self.create_label(f"Name: {name}", 6, 0))
        self.labels.append(self.create_label(f"Platform: {platform}", 7, 0))

        # Update level label
        self.level_label.config(text=f"Level: {level}")

        # Create a label with different color based on rankName
        rank_name_label = self.create_label(f"Rank Name: {rankName}", 8, 0)
        rank_LP_label = self.create_label(f"LP: {formatNumber(rankScore)}", 9, 0)
        if rankName == "Bronze":
            rank_name_label.config(fg="brown")
        elif rankName == "Silver":
            rank_name_label.config(fg="gray")
        elif rankName == "Gold":
            rank_name_label.config(fg="gold")
        elif rankName == "Platinum":
            rank_name_label.config(fg="light blue")
        elif rankName == "Diamond":
            rank_name_label.config(fg="blue")
        elif rankName == "Master":
            rank_name_label.config(fg="purple")
        elif rankName == "Apex Predator":
            rank_name_label.config(fg="red")

        self.labels.append(rank_name_label)
        self.labels.append(rank_LP_label)
        self.labels.append(self.create_label(f"Legend Name: {LegendName}", 10, 0))

        for i, tracker in enumerate(LegendData[:3]):
            trackerName = tracker["name"]
            trackerValue = tracker["value"]
            self.labels.append(self.create_label(f"{trackerName}: {trackerValue}", 11 + i, 0))

    def create_label(self, text, row, column):
        """Create a label with the given text and grid position."""
        label = tk.Label(self, text=text)
        label.grid(row=row, column=column, sticky='w')
        return label


def formatNumber(NUMBER):
    return "{:,.0f}".format(NUMBER)
