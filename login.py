import tkinter as tk
from tkinter import messagebox
from user_functions import UserFunctions
from account_settings import AccountSettings
from transfer import Transfer

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")

    def login_window(self):
        tk.Label(self.root, text="Email").grid(row=0, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=0, column=1)

        tk.Label(self.root, text="PIN (6 digits)").grid(row=1, column=0)
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Login", command=self.login).grid(row=2, columnspan=2)

        self.root.mainloop()

    def login(self):
        email = self.email_entry.get()
        pin = self.pin_entry.get()

        # Check credentials in the database
        user_functions = UserFunctions()
        if user_functions.authenticate(email, pin):
            messagebox.showinfo("Login Successful", "Welcome to the system!")
            self.root.destroy()
            self.open_account_settings(email)
        else:
            messagebox.showerror("Login Failed", "Invalid email or PIN.")

    def open_account_settings(self, email):
        account_settings = AccountSettings(email)
        account_settings.account_settings_window()
        account_settings = Transfer(email)
        account_settings.transfer_window()

if __name__ == "__main__":
    login = Login()
    login.login_window()
