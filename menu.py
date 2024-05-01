import tkinter as tk
from user_functions import UserFunctions
from create_account import CreateAccount
from account_settings import AccountSettings
from transfer import Transfer
from login import Login

class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Banking System")
    
    def display_menu(self):
        tk.Label(self.root, text="Welcome to Banking System").pack()
        tk.Button(self.root, text="Create Account", command=self.open_create_account).pack()
        tk.Button(self.root, text="Account Settings", command=self.open_account_settings).pack()
        tk.Button(self.root, text="Transfer", command=self.open_transfer).pack()

        self.root.mainloop()

    def open_create_account(self):
        create_account = CreateAccount()
        create_account.create_account_window()

    def open_account_settings(self):
        login = Login()
        login.login_window()

    def open_transfer(self):
        login = Login()
        login.login_window()

if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()
