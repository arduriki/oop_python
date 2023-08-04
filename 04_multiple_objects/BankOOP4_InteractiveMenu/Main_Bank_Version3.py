# Interactive test program creating a dictionary of accounts
# Version 4, with an interactive menu

from Account import Account

accountsDict = {}
nextAccountNumber = 0

# Build some starting accounts for testing
oAccount = Account('Joe', 100, 'JoesPassword')
accountsDict[nextAccountNumber] = oAccount
print('Account number for Joe is:', nextAccountNumber)
# increment the account number after assignment
nextAccountNumber += 1

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsDict[nextAccountNumber] = oAccount
print('Account number for Mary is:', nextAccountNumber)
nextAccountNumber += 1

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ').lower()
    action = action[0]  # grab the first letter
    print()

    if action == 'b':
        print('*** Get Balance ***')
        userAccountNumber = int(input('Please enter your account number: '))
        userAccountPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('*** Deposit ***')
        userAccountNumber = int(input('Please enter your account number: '))
        userDepositAmount = int(input('Please enter amount to deposit: '))
        userPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)

    elif action == 'o':
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = int(input('What is the starting balance for this account? '))
        userPassword = input('What is the password you want to use for this account? ')
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print('Your new account number is:', nextAccountNumber)
        nextAccountNumber += 1
        print()

    elif action == 's':
        print('Show:')
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print('    Account number:', userAccountNumber)
            oAccount.show()  # userAccountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Withdraw ***')
        userAccountNumber = int(input('Please enter your account number: '))
        userWithdrawalAmount = int(input('Please enter the amount to withdraw: '))
        userPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)
        if theBalance is not None:
            print('Withdrew:', userWithdrawalAmount)
            print('Your new balance is:', theBalance)

    else:
        print('Sorry that was not a valid action. Please try again.')

print('Done')
