import tkinter as tk
from tkinter import messagebox
from user_functions import UserFunctions

class Transfer:
    def __init__(self, email):
        self.email = email
        self.user_functions = UserFunctions()
        self.root = tk.Tk()
        self.root.title("Transfer")

        self.display_balance()

    def display_balance(self):
        balance = self.user_functions.check_balance(self.email)
        if balance is not None:
            tk.Label(self.root, text=f"Your current balance is: ${balance}").pack()
            tk.Label(self.root, text="Enter amount to transfer:").pack()
            self.amount_entry = tk.Entry(self.root)
            self.amount_entry.pack()
            tk.Button(self.root, text="Transfer", command=self.transfer).pack()
        else:
            tk.Label(self.root, text="Failed to retrieve balance").pack()

    def transfer(self):
        amount = self.amount_entry.get()
        if amount:
            success = self.user_functions.transfer(self.email, amount)
            if success:
                messagebox.showinfo("Success", f"${amount} transferred successfully.")
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Transfer failed. Insufficient balance.")
        else:
            messagebox.showerror("Error", "Please enter an amount to transfer.")

    def run(self):
        self.root.mainloop()
