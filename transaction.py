from datetime import datetime

class Transaction:
    def __init__(self, account):
        self.account = account
        self.daily_limit = 10000  # Daily transaction limit

    def apply_interest(self):
        last_applied = datetime.fromisoformat(self.account['last_interest_applied'])
        now = datetime.now()
        days_passed = (now - last_applied).days

        if days_passed >= 365:  # Apply interest yearly
            interest = self.account['balance'] * self.account['interest_rate']
            self.account['balance'] += interest
            self.account['history'].append(f"Interest applied: ${interest:.2f}")
            self.account['last_interest_applied'] = str(now)

    def deposit(self, amount):
        today = datetime.now().date()
        transactions_today = sum(1 for t in self.account['history'] if t.startswith(f"Deposited: on {today}"))

        if transactions_today < 3:
            if amount > 0 and amount <= self.daily_limit:
                self.account['balance'] += amount
                self.account['history'].append(f"Deposited: ${amount:.2f} on {today}")
                return True
            else:
                return False
        else:
            self.account['balance'] += amount - 50  # Fee for exceeding limit
            self.account['history'].append(f"Deposited: ${amount:.2f} (Fee: $50 applied) on {today}")
            return True

    def withdraw(self, amount):
        today = datetime.now().date()
        transactions_today = sum(1 for t in self.account['history'] if t.startswith(f"Withdrew: on {today}"))

        if transactions_today < 3:
            if 0 < amount <= self.account['balance']:
                self.account['balance'] -= amount
                self.account['history'].append(f"Withdrew: ${amount:.2f} on {today}")
                return True
            else:
                return False
        else:
            if 0 < amount + 50 <= self.account['balance']:  # Fee for exceeding limit
                self.account['balance'] -= amount + 50
                self.account['history'].append(f"Withdrew: ${amount:.2f} (Fee: $50 applied) on {today}")
                return True
            return False

    def get_history(self):
        return self.account['history']
