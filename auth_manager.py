from file_manager import FileManager
from datetime import datetime

class Authentication:
    def __init__(self):
        self.file_manager = FileManager()
        self.data = self.file_manager.load_data()

    def signup(self, username, password):
        account_type = input("Choose account type (savings/checking): ").lower()
        if account_type not in ['savings', 'checking']:
            account_type = 'savings'  # Default to savings if invalid input
        if username not in self.data:
            self.data[username] = {
                "password": password,
                "balance": 0,
                "history": [],
                "interest_rate": 0.02 if account_type == "savings" else 0.01,  # 2% for savings, 1% for checking
                "last_interest_applied": str(datetime.now())
            }
            self.file_manager.save_data(self.data)
            return True
        return False

    def login(self, username, password):
        if username in self.data and self.data[username]["password"] == password:
            return True
        return False

    def get_account(self, username):
        return self.data[username]
