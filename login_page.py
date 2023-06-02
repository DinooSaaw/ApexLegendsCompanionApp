import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, parent, login_callback):
        super().__init__(parent)
        self.login_callback = login_callback

        # Create login form
        label_username = tk.Label(self, text="Username:")
        label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        label_password = tk.Label(self, text="Password:")
        label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        button_login = tk.Button(self, text="Login", command=self.login)
        button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Perform login validation (replace with your own logic)
        if username == "admin" and password == "password":
            print(f"Login successful. Username: {username}")
            self.login_callback(username)
        else:
            self.entry_username.delete(0, tk.END)  # Clear username entry
            self.entry_password.delete(0, tk.END)  # Clear password entry