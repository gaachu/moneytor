class Transaction:
    def __init__(self, date, amount, category):
        self.date = date
        self.amount = amount
        self.category = category

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount, category):
        self.balance += amount
        transaction = Transaction(datetime.now(), amount, category)
        self.transactions.append(transaction)

    def withdraw(self, amount, category):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount
            transaction = Transaction(datetime.now(), -amount, category)
            self.transactions.append(transaction)

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

class Budget:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.spent = 0
        self.transactions = []

    def add_transaction(self, amount):
        self.spent += amount
        transaction = Transaction(datetime.now(), amount, self.name)
        self.transactions.append(transaction)

    def get_amount_left(self):
        return self.amount - self.spent

    def get_transactions(self):
        return self.transactions

class MONEYTOR:
    def __init__(self):
        self.accounts = []
        self.budgets = []

    def add_account(self, name, balance=0):
        account = Account(name, balance)
        self.accounts.append(account)

    def add_budget(self, name, amount):
        budget = Budget(name, amount)
        self.budgets.append(budget)

    def get_account_balance(self, account_name):
        for account in self.accounts:
            if account.name == account_name:
                return account.get_balance()
        return None

    def get_account_transactions(self, account_name):
        for account in self.accounts:
            if account.name == account_name:
                return account.get_transactions()
        return None

    def get_budget_amount_left(self, budget_name):
        for budget in self.budgets:
            if budget.name == budget_name:
                return budget.get_amount_left()
        return None

    def get_budget_transactions(self, budget_name):
        for budget in self.budgets:
            if budget.name == budget_name:
                return budget.get_transactions()
        return None




