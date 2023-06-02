import tkinter as tk

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

        # Add text to each page
        if page == self.stats_page:
            label = tk.Label(page, text="Welcome to the Stats Page")
            label.pack()
        
        elif page == self.leaderboard_page:
            label = tk.Label(page, text="Welcome to the Leaderboard Page")
            label.pack()
        
        elif page == self.home_page:
            label = tk.Label(page, text="Welcome to the Home Page")
            label.pack()

# Run the application
app = Application()
app.mainloop()
