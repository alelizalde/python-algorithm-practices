from bank.Account import Account

act01 = Account(owner="Al", balance=500)
act01.deposit(100)
print(act01)
act01.withdraw(300)
print(act01)
act01.withdraw(300)
print(act01)
act01.withdraw(300)
