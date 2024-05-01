import tkinter as tk
from tkinter import messagebox
from user_functions import UserFunctions

class AccountSettings:
    def __init__(self, email):
        self.email = email
        self.user_functions = UserFunctions()
        self.root = tk.Tk()
        self.root.title("Account Settings")
        
        self.populate_user_info()

    def populate_user_info(self):
        user_info = self.user_functions.get_user_info(self.email)
        if user_info:
            tk.Label(self.root, text="First Name").grid(row=0, column=0)
            self.first_name_entry = tk.Entry(self.root)
            self.first_name_entry.grid(row=0, column=1)
            self.first_name_entry.insert(0, user_info["first_name"])

            tk.Label(self.root, text="Last Name").grid(row=1, column=0)
            self.last_name_entry = tk.Entry(self.root)
            self.last_name_entry.grid(row=1, column=1)
            self.last_name_entry.insert(0, user_info["last_name"])

            tk.Label(self.root, text="Email").grid(row=2, column=0)
            self.email_entry = tk.Entry(self.root)
            self.email_entry.grid(row=2, column=1)
            self.email_entry.insert(0, user_info["email"])

            tk.Label(self.root, text="Phone Number").grid(row=3, column=0)
            self.phone_entry = tk.Entry(self.root)
            self.phone_entry.grid(row=3, column=1)
            self.phone_entry.insert(0, user_info["phone"])

            tk.Button(self.root, text="Save Changes", command=self.save_changes).grid(row=4, columnspan=2)
        else:
            tk.Label(self.root, text="User not found").pack()

    def save_changes(self):
        new_first_name = self.first_name_entry.get()
        new_last_name = self.last_name_entry.get()
        new_email = self.email_entry.get()
        new_phone = self.phone_entry.get()

        new_settings = {
            "first_name": new_first_name,
            "last_name": new_last_name,
            "email": new_email,
            "phone": new_phone
        }

        self.user_functions.update_account_
