# Person example main program using direct access
# The first version of the class is without functions

from Person import *
from PrivatePerson import *

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# Get the values of the salary variable directly
print(oPerson1.getSalary())
print(oPerson2.getSalary())

# Change the salary variable directly
oPerson1.setSalary(100000)
oPerson2.setSalary(111111)

# Get the updated salaries and print again
print(oPerson1.getSalary())
print(oPerson2.getSalary())

oPrivatePerson = PrivatePerson('Jordi Ardura', 'some private data')

usersPrivateData = oPrivatePerson._PrivatePerson__privateData