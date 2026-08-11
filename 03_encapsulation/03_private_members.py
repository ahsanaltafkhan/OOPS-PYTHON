class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def show_balance(self):
        print(self.__balance)
    def deposit(self, amount):
        self.__balance += amount
account = BankAccount(5000)
account.show_balance()
account.deposit(2000)
account.show_balance()