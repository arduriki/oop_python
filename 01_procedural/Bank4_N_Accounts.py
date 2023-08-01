# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

accountNamesList = []
accountBalancesList = []
accountPasswordsList = []


def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account', accountNumber)
    print('        Name', accountNamesList[accountNumber])
    print('        Balance:', accountBalancesList[accountNumber])
    print('        Password:', accountPasswordsList[accountNumber])
    print()


def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]


def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None

    accountBalancesList[accountNumber] += amountToDeposit
    return accountBalancesList[accountNumber]


def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPasswordsList[accountNumber]:
        return None

    if amountToWithdraw > accountBalancesList[accountNumber]:
        print('You cannot withdraw more than you have in your acocunt')
        return None

    accountBalancesList[accountNumber] -= amountToWithdraw
    return accountBalancesList[accountNumber]


# Create two sample accounts
print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ').lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userAccountNumber = int(input('Please enter your account number: '))
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('You balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber = int(input('Please enter your account number: '))
        userDepositAmount = int(input('Please enter amount to deposit: '))
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = int(input('What is the amount of your initial deposit? '))
        userPassword = input('What password would you like to use for this account? ')

        userAccountNumber = len(accountNamesList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    elif action == 's':  # show all
        print('Show:')
        nAccounts = len(accountNamesList)
        for accountNumber in range(0, nAccounts):
            show(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdrawal')
        userAccountNumber = int(input('Please enter your account number: '))
        userWithdrawalAmount = int(input('Please enter the amount to withdraw: '))
        userPassword = input('Please enter the password: ')

        newBalance = withdraw(userAccountNumber, userWithdrawalAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

print('Done')