import tkinter as tk
from tkinter import messagebox
from user_functions import UserFunctions

class CreateAccount:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Create Account")

    def create_account_window(self):
        # tk.Label(self.root, text="Create Account").pack()
        # create_account_window = tk.Toplevel(self.root)
        # Add your code for creating the account window here

        # Account Number
        tk.Label(self.root, text="Account Number").grid(row=0, column=0)
        tk.Entry(self.root).grid(row=0, column=1)

        # PIN
        tk.Label(self.root, text="PIN (6 digits)").grid(row=1, column=0)
        tk.Entry(self.root).grid(row=1, column=1)

        # First Name
        tk.Label(self.root, text="First Name").grid(row=2, column=0)
        tk.Entry(self.root).grid(row=2, column=1)

        # Last Name
        tk.Label(self.root, text="Last Name").grid(row=3, column=0)
        tk.Entry(self.root).grid(row=3, column=1)

        # Initial Balance
        tk.Label(self.root, text="Initial Balance").grid(row=4, column=0)
        tk.Entry(self.root).grid(row=4, column=1)

        # Email
        tk.Label(self.root, text="Email").grid(row=5, column=0)
        tk.Entry(self.root).grid(row=5, column=1)

        # Phone Number
        tk.Label(self.root, text="Phone Number").grid(row=6, column=0)
        tk.Entry(self.root).grid(row=6, column=1)

        # Date of Birth
        tk.Label(self.root, text="Date of Birth (YYYY-MM-DD)").grid(row=7, column=0)
        tk.Entry(self.root).grid(row=7, column=1)

        # Create Account Button
        tk.Button(self.root, text="Create Account", command=self.create_account).grid(row=8, columnspan=2)

        self.root.mainloop()

    def create_account(self):
        messagebox.showinfo("Account Created", "Account created successfully.")

if __name__ == "__main__":
    create_account = CreateAccount()
    create_account.create_account_window()
    create_account.geometry("400x300")
