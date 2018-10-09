class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = int(balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to {self.owner} balance")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {amount} to {self.owner} balance completed")
        else:
            print("Withdraw amount exceed balance")

    def __str__(self):
        return f"The balance for {self.owner} is {self.balance}"
