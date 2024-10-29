class Accounts:
    def __init__(self, account_data):
        self.account_data = account_data

    def check_balance(self):
        return self.account_data['balance']

    def get_account_type(self):
        return "savings" if self.account_data['interest_rate'] == 0.02 else "checking"

    def get_account_details(self):
        return self.account_data
