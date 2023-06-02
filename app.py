import tkinter as tk

class StatsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Stats Page")
        label.pack()

class LeaderboardPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Leaderboard Page")
        label.pack()

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Welcome to the Home Page")
        label.pack()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Game App")
        self.geometry("400x300")
        
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
        
        # Create page containers
        self.stats_page = None
        self.leaderboard_page = None
        self.home_page = None
        
        self.current_page = None
        
        # Show home page by default
        self.open_home_page()
    
    def open_stats_page(self):
        if self.current_page:
            self.current_page.pack_forget()
            
        if self.stats_page is None:
            self.stats_page = StatsPage(self)
        
        self.stats_page.pack()
        self.current_page = self.stats_page
        
    def open_leaderboard_page(self):
        if self.current_page:
            self.current_page.pack_forget()
            
        if self.leaderboard_page is None:
            self.leaderboard_page = LeaderboardPage(self)
        
        self.leaderboard_page.pack()
        self.current_page = self.leaderboard_page
        
    def open_home_page(self):
        if self.current_page:
            self.current_page.pack_forget()
            
        if self.home_page is None:
            self.home_page = HomePage(self)
        
        self.home_page.pack()
        self.current_page = self.home_page

# Run the application
app = Application()
app.mainloop()
