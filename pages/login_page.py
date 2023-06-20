import tkinter as tk
from database import connect_to_mongodb, find_documents

# Establish connection to MongoDB
client = connect_to_mongodb()

# Get a reference to the desired collection
db = client["ALC"]
collection = db["users"]

class LoginPage(tk.Frame):
    """Class representing the Login Page of the application."""

    def __init__(self, parent, login_callback):
        """Initialize the Login Page.

        Args:
            parent (tk.Widget): The parent widget.
            login_callback (function): The callback function to handle login events.
        """
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
        """Perform login based on the entered username and password."""
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Perform login validation
        query = {"username": username}
        results = find_documents(collection, query)

        try:
            first_result = results.next()
            stored_password = first_result["password"]

            if password == stored_password:
                print(f"Login successful. Logged in as {username}")
                self.login_callback(username, first_result["accessLevel"])
            else:
                self.entry_username.delete(0, tk.END)  # Clear username entry
                self.entry_password.delete(0, tk.END)  # Clear password entry
                print("Invalid username or password")

        except StopIteration:
            self.entry_username.delete(0, tk.END)  # Clear username entry
            self.entry_password.delete(0, tk.END)  # Clear password entry
            print("Invalid username or password")