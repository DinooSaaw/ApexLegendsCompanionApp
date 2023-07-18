import contextlib
import tkinter as tk
from tkinter import messagebox
import json
from pages.stats_page import StatsPage
from pages.leaderboard_page import LeaderboardPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import Config


class GameApp(tk.Tk):
    """Main application class for the game."""

    def __init__(self):
        """Initialize the GameApp class."""
        super().__init__()

        self.title(Config.WINDOW_TITLE)
        self.geometry(Config.WINDOW_SIZE)
        self.iconbitmap(Config.ICON_PATH)
        self.setup_ui()

        # Set up variables
        self.current_page = None
        self.username = ""

        # Create page containers
        self.stats_page = StatsPage(self)
        self.leaderboard_page = LeaderboardPage(self)
        self.home_page = HomePage(self)
        self.login_page = LoginPage(self, self.login)

        self.load_data()  # Load user data from file

        self.open_login_page()

    def setup_ui(self):
        """Set up the user interface."""
        # Create a frame for buttons
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, pady=10)

        # Create buttons and place them in the frame
        self.stats_button = tk.Button(
            button_frame, text="Stats", command=self.open_stats_page)
        self.stats_button.pack(side=tk.LEFT, padx=10)

        self.leaderboard_button = tk.Button(
            button_frame, text="Leaderboard", command=self.open_leaderboard_page)
        self.leaderboard_button.pack(side=tk.LEFT, padx=10)

        self.home_button = tk.Button(
            button_frame, text="Home", command=self.open_home_page)
        self.home_button.pack(side=tk.LEFT, padx=10)

        # Create a label to display the username
        self.username_label = tk.Label(
            self, text="Not Logged In", font=("Arial", 10))
        self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)

    def open_stats_page(self):
        """Switch to the Stats page."""
        self.switch_page(self.stats_page, "Stats")

    def open_leaderboard_page(self):
        """Switch to the Leaderboard page."""
        self.switch_page(self.leaderboard_page, "Leaderboard")

    def open_home_page(self):
        """Switch to the Home page."""
        self.switch_page(self.home_page, "Home")

    def open_login_page(self):
        """Switch to the Login page."""
        self.switch_page(self.login_page, "Login")

    def switch_page(self, page, page_title):
        """Switch to the specified page.

        Args:
            page: The page to switch to.
            page_title: The title of the page.

        """
        if self.current_page:
            self.current_page.pack_forget()

        page.pack()
        self.current_page = page
        self.update_title(page_title)

    def update_title(self, page_title):
        """Update the application title.

        Args:
            page_title: The new title for the application.

        """
        self.title(f"ALC ~ {page_title}")

    def login(self, username):
        """Perform the login operation."""
        self.username = username
        self.username_label.config(text=f"Logged In as {username}")
        self.open_home_page()
        self.save_data()  # Save user data to file

    def save_data(self):
        """Save user data to a file."""
        data = {"username": self.username}
        with open("user_data.json", "w") as file:
            json.dump(data, file)

    def load_data(self):
        """Load user data from a file."""
        with contextlib.suppress(FileNotFoundError):
            with open("user_data.json", "r") as file:
                data = json.load(file)
                self.username = data.get("username", "")


def check_stored_credentials(self, username):
    """Check if stored credentials for the given username are valid."""
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
            if username in accounts:
                return True
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist or hasn't been created yet
    except json.JSONDecodeError:
        pass  # Ignore if there's an issue decoding the JSON data
    return False


# Run the application
if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
