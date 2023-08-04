# Bank that manages a dictionary of Account objects

from Account import *


class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.nextAccountNumber += 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ').title()
        userStartingAmount = int(input('What is the starting balance for this account? '))
        userPassword = input('What password would you want to use for this account? ')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = int(input('What is your account number? '))
        userPassword = input('What is your password? ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)

        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is being return to you.')
            # Remove user's account from the dictionary of accounts
            del self.accountsDict[userAccountNumber]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = int(input('Please enter your account number: '))
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = int(input('Please enter the account number: '))
        depositAmount = int(input('Please enter amount to deposit: '))
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[accountNum]
        theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('    Account number:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = int(input('Please enter your account number: '))
        userAmount = int(input('Please enter the amount to withdraw: '))
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Withdrew:', userAmount)
            print('Your new balance is:', theBalance)

    def bankInfo(self):
        print('Hours: 9 to 5')
        print('Address: 123 Main Street, Anytown, USA')
        print('Phone:  (650) 555-1212')
        print('We currently have', len(self.accountsDict), 'account(s) open.')
