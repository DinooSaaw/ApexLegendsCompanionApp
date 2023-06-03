import tkinter as tk
from stats_page import StatsPage
from leaderboard_page import LeaderboardPage
from home_page import HomePage
from login_page import LoginPage
accessLevel = 0

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Game App")
        self.geometry("400x300")

        # Create a frame for buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Create buttons and place them in the frame
        self.stats_button = tk.Button(
            button_frame, text="Stats", command=self.open_stats_page)
        self.stats_button.grid(row=0, column=0, padx=10)

        self.leaderboard_button = tk.Button(
            button_frame, text="Leaderboard", command=self.open_leaderboard_page)
        self.leaderboard_button.grid(row=0, column=1, padx=10)

        self.home_button = tk.Button(
            button_frame, text="Home", command=self.open_home_page)
        self.home_button.grid(row=0, column=2, padx=10)

        # Create page containers
        self.stats_page = None
        self.leaderboard_page = None
        self.home_page = None
        self.login_page = None

        self.current_page = None
        self.is_konami_code_active = False
        self.is_logged_in = False  # Variable to track login status

        # Create a label to display the username
        self.username_label = tk.Label(self, text="Not Logged In", font=("Arial", 10))
        self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)

        # Create the login button
        self.login_button = tk.Button(
            self, text="Login", command=self.open_login_page)

        # Show home page by default
        self.open_home_page()

    def open_stats_page(self):
        if self.current_page:
            self.current_page.pack_forget()

        if self.stats_page is None:
            self.stats_page = StatsPage(self)

        self.stats_page.pack()
        self.current_page = self.stats_page
        self.update_title("Stats")

    def open_leaderboard_page(self):
        if self.current_page:
            self.current_page.pack_forget()

        if self.leaderboard_page is None:
            self.leaderboard_page = LeaderboardPage(self)

        self.leaderboard_page.pack()
        self.current_page = self.leaderboard_page
        self.update_title("Leaderboard")

    def open_home_page(self):
        if self.current_page:
            self.current_page.pack_forget()

        if self.is_logged_in:
            self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)
        else:
            self.username_label.pack_forget()

        self.login_button.pack_forget()  # Hide the login button

        if self.home_page is None:
            self.home_page = HomePage(self, self.konami_code_callback)

        self.home_page.pack()
        self.current_page = self.home_page
        self.update_title("Home")

    def open_login_page(self):
        if self.current_page:
            self.current_page.pack_forget()

        if self.login_page is None:
            self.login_page = LoginPage(self, self.login_callback)

        self.login_page.pack()
        self.current_page = self.login_page
        self.update_title("Login")

    def update_title(self, page_title):
        self.title(f"Game App ~ {page_title}")

    def konami_code_callback(self):
        self.is_konami_code_active = True
        self.login_button.pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10)

    def login_callback(self, username, accessLevel):
        self.is_logged_in = True
        accessLevel = accessLevel
        self.username_label.config(text=f"Logged In as {username}")
        self.open_home_page()
        self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)
        self.login_button.pack_forget()  # Hide the login button after successful login


# Run the application
app = Application()
app.mainloop()
