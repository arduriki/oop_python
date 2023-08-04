# Account class

class Account():
    def __init__(self, name, balance, password):
        self.name = name.title()
        self.balance = int(balance)
        self.password = password

    def deposit(self, amoutToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amoutToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None

        self.balance += amoutToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None

        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return None

        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance

    # Added for debugging
    def show(self):
        print('     Name:', self.name)
        print('     Balance:', self.balance)
        print('     Password:', self.password)
        print()