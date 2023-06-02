import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Game App")
        self.geometry("400x300")
        
        # Create buttons
        self.stats_button = tk.Button(self, text="Stats", command=self.open_stats_page)
        self.stats_button.pack(pady=10)
        
        self.leaderboard_button = tk.Button(self, text="Leaderboard", command=self.open_leaderboard_page)
        self.leaderboard_button.pack(pady=10)
        
        self.home_button = tk.Button(self, text="Home", command=self.open_home_page)
        self.home_button.pack(pady=10)
        
        # Create page containers
        self.stats_page = tk.Frame(self)
        self.leaderboard_page = tk.Frame(self)
        self.home_page = tk.Frame(self)
        
        self.current_page = None
        
        # Show home page by default
        self.open_home_page()
    
    def open_stats_page(self):
        self.show_page(self.stats_page)
        
    def open_leaderboard_page(self):
        self.show_page(self.leaderboard_page)
        
    def open_home_page(self):
        self.show_page(self.home_page)
        
    def show_page(self, page):
        if self.current_page:
            self.current_page.pack_forget()
            
        page.pack()
        self.current_page = page

# Run the application
app = Application()
app.mainloop()