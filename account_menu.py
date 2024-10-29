import tkinter as tk
from tkinter import messagebox, simpledialog
from auth_manager import Authentication
from account import Accounts
from transaction import Transaction

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Banking Dashboard")
        self.master.geometry("400x400")

        # Initialize authentication
        self.auth = Authentication()
        self.current_user = None

        # Dashboard UI
        self.label = tk.Label(master, text="Welcome to the Banking System", font=("Arial", 16))
        self.label.pack(pady=10)

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.signup_button = tk.Button(master, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=5)

    def login(self):
        username = simpledialog.askstring("Input", "Enter Username:")
        password = simpledialog.askstring("Input", "Enter Password:", show='*')
        if self.auth.login(username, password):
            self.current_user = username
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Login failed. Try again.")

    def signup(self):
        username = simpledialog.askstring("Input", "Choose Username:")
        password = simpledialog.askstring("Input", "Choose Password:", show='*')
        if self.auth.signup(username, password):
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showerror("Error", "Username already exists!")

    def show_dashboard(self):
        self.clear_screen()

        self.label = tk.Label(self.master, text=f"Welcome, {self.current_user}", font=("Arial", 16))
        self.label.pack(pady=10)

        self.balance_button = tk.Button(self.master, text="Check Balance", command=self.check_balance)
        self.balance_button.pack(pady=5)

        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(self.master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.history_button = tk.Button(self.master, text="Transaction History", command=self.show_history)
        self.history_button.pack(pady=5)

        self.account_type_button = tk.Button(self.master, text="Account Type", command=self.show_account_type)
        self.account_type_button.pack(pady=5)

        self.apply_interest_button = tk.Button(self.master, text="Apply Interest", command=self.apply_interest)
        self.apply_interest_button.pack(pady=5)

        self.logout_button = tk.Button(self.master, text="Logout", command=self.logout)
        self.logout_button.pack(pady=20)

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def check_balance(self):
        account = Accounts(self.auth.get_account(self.current_user))
        balance = account.check_balance()
        messagebox.showinfo("Balance", f"Your current balance is: ${balance:.2f}")

    def deposit(self):
        account = Accounts(self.auth.get_account(self.current_user))
        transaction = Transaction(account.get_account_details())
        amount = float(simpledialog.askstring("Input", "Enter amount to deposit:"))
        if transaction.deposit(amount):
            messagebox.showinfo("Success", f"Deposited ${amount:.2f}")
        else:
            messagebox.showerror("Error", "Invalid amount.")

    def withdraw(self):
        account = Accounts(self.auth.get_account(self.current_user))
        transaction = Transaction(account.get_account_details())
        amount = float(simpledialog.askstring("Input", "Enter amount to withdraw:"))
        if transaction.withdraw(amount):
            messagebox.showinfo("Success", f"Withdrew ${amount:.2f}")
        else:
            messagebox.showerror("Error", "Insufficient balance or invalid amount.")

    def show_history(self):
        account = Accounts(self.auth.get_account(self.current_user))
        transaction = Transaction(account.get_account_details())
        history = "\n".join(transaction.get_history())
        messagebox.showinfo("Transaction History", history)

    def show_account_type(self):
        account = Accounts(self.auth.get_account(self.current_user))
        account_type = account.get_account_type()
        messagebox.showinfo("Account Type", f"Your account type is: {account_type}")

    def apply_interest(self):
        account = Accounts(self.auth.get_account(self.current_user))
        transaction = Transaction(account.get_account_details())
        transaction.apply_interest()
        messagebox.showinfo("Interest", "Interest applied if applicable.")

    def logout(self):
        self.current_user = None
        self.clear_screen()
        self.label = tk.Label(self.master, text="Welcome to the Banking System", font=("Arial", 16))
        self.label.pack(pady=10)

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.signup_button = tk.Button(self.master, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=5)
