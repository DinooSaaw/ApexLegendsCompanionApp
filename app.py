import tkinter as tk
from stats_page import StatsPage
from leaderboard_page import LeaderboardPage
from home_page import HomePage
from login_page import LoginPage
from settings_page import SettingsPage

class GameApp(tk.Tk):
    """Main application class for the game."""

    def __init__(self):
        """Initialize the GameApp class."""
        super().__init__()

        self.title("ALC")
        self.geometry("600x400")
        icon_path = "./assests/icon.ico"
        self.iconbitmap(icon_path)
        self.setup_ui()

        # Create page containers
        self.stats_page = StatsPage(self)
        self.leaderboard_page = LeaderboardPage(self)
        self.home_page = HomePage(self, self.konami_code_callback)
        self.login_page = LoginPage(self, self.login_callback)
        self.settings_page = SettingsPage(self)

        # Set up variables
        self.current_page = None
        self.is_konami_code_active = False
        self.is_logged_in = False
        self.access_level = 0

        self.open_home_page()

    def setup_ui(self):
        """Set up the user interface."""
        # Create a frame for buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Create buttons and place them in the frame
        self.stats_button = tk.Button(button_frame, text="Stats", command=self.open_stats_page)
        self.stats_button.grid(row=0, column=0, padx=10)

        self.leaderboard_button = tk.Button(button_frame, text="Leaderboard", command=self.open_leaderboard_page)
        self.leaderboard_button.grid(row=0, column=1, padx=10)

        self.home_button = tk.Button(button_frame, text="Home", command=self.open_home_page)
        self.home_button.grid(row=0, column=2, padx=10)

        # Create a label to display the username
        self.username_label = tk.Label(self, text="Not Logged In", font=("Arial", 10))
        self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)

        # Create the login button
        self.login_button = tk.Button(self, text="Login", command=self.open_login_page)

        # Create the settings button
        self.settings_button = tk.Button(self, text="⚙️", command=self.open_settings_page)
        self.settings_button.place(x=self.winfo_width() - 60, y=0)

    def open_stats_page(self):
        """Switch to the Stats page."""
        self.switch_page(self.stats_page, "Stats")

    def open_leaderboard_page(self):
        """Switch to the Leaderboard page."""
        self.switch_page(self.leaderboard_page, "Leaderboard")

    def open_home_page(self):
        """Switch to the Home page."""
        if self.is_logged_in:
            self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)
            if self.access_level >= 3:
                self.settings_button.place(x=self.winfo_width() - 60, y=0)
            else:
                self.settings_button.place_forget()
        else:
            self.username_label.pack_forget()
            self.settings_button.place_forget()

        self.login_button.pack_forget()

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

    def konami_code_callback(self):
        """Callback function for Konami code activation."""
        self.is_konami_code_active = True
        self.login_button.pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10)

    def login_callback(self, username, access_level):
        """Callback function for successful login.

        Args:
            username: The logged-in user's username.
            access_level: The access level of the user.

        """
        self.is_logged_in = True
        self.access_level = access_level
        self.username_label.config(text=f"Logged In as {username}")
        self.open_home_page()
        self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)
        self.login_button.pack_forget()

    def open_settings_page(self):
        """Switch to the Settings page."""
        self.switch_page(self.settings_page, "Settings")

# Run the application
if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
