import tkinter as tk
from stats_page import StatsPage
from leaderboard_page import LeaderboardPage
from home_page import HomePage
from login_page import LoginPage

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ALC")
        self.geometry("400x300")
        icon_path = "./assests/icon.ico"
        self.iconbitmap(icon_path)
        self.setup_ui()

        # Create page containers
        self.stats_page = StatsPage(self)
        self.leaderboard_page = LeaderboardPage(self)
        self.home_page = HomePage(self, self.konami_code_callback)
        self.login_page = LoginPage(self, self.login_callback)

        self.current_page = None
        self.is_konami_code_active = False
        self.is_logged_in = False
        self.access_level = 0

        self.open_home_page()

    def setup_ui(self):
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

        # Create a label to display the username
        self.username_label = tk.Label(self, text="Not Logged In", font=("Arial", 10))
        self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)

        # Create the login button
        self.login_button = tk.Button(
            self, text="Login", command=self.open_login_page)

    def open_stats_page(self):
        self.switch_page(self.stats_page, "Stats")

    def open_leaderboard_page(self):
        self.switch_page(self.leaderboard_page, "Leaderboard")

    def open_home_page(self):
        if self.is_logged_in:
            self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)
        else:
            self.username_label.pack_forget()

        self.login_button.pack_forget()

        self.switch_page(self.home_page, "Home")

    def open_login_page(self):
        self.switch_page(self.login_page, "Login")

    def switch_page(self, page, page_title):
        if self.current_page:
            self.current_page.pack_forget()

        page.pack()
        self.current_page = page
        self.update_title(page_title)

    def update_title(self, page_title):
        self.title(f"ALC ~ {page_title}")

    def konami_code_callback(self):
        self.is_konami_code_active = True
        self.login_button.pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10)

    def login_callback(self, username, access_level):
        self.is_logged_in = True
        self.access_level = access_level
        self.username_label.config(text=f"Logged In as {username}")
        self.open_home_page()
        self.username_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)
        self.login_button.pack_forget()


# Run the application
if __name__ == "__main__":
    app = GameApp()
    app.mainloop()