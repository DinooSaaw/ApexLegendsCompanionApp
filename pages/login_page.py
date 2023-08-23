import tkinter as tk
import bcrypt
import json
from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, parent, login_callback):
        super().__init__(parent)
        self.login_callback = login_callback

        self.username_label = tk.Label(self, text="Username:", font=("Arial", 12))
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self, font=("Arial", 12))
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self, text="Password:", font=("Arial", 12))
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=10)

        self.login_button = tk.Button(self, text="Login", font=("Arial", 12), command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username and password:
            if self.validate_credentials(username, password):
                self.login_callback(username)
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Invalid Credentials", "Invalid username or password.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid username and password.")

    def validate_credentials(self, username, password):
        with open("accounts.json", "r") as file:
            accounts = json.load(file)

        if username in accounts:
            stored_hash = accounts[username]
            input_password = password.encode('utf-8')
            return bcrypt.checkpw(input_password, stored_hash.encode('utf-8'))
        else:
            return False