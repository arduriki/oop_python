from Account import Account

# Instantiate an object with three arguments
oAccount = Account('joe schmoe', 1000, 'magic')
# Make a deposit with two arguments for the parameters
newBalance = oAccount.deposit(500, 'magic')
# Make a withdrawal:
oAccount.withdraw(250, 'magic')
# Check the balance:
currentBalance = oAccount.getBalance('magic')
# Show details:
print(newBalance)
print(currentBalance)
oAccount.show()