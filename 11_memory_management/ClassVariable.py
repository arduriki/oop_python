# Sample class

class Sample():
    nObjects = 0  # this is a class variable of the Sample class

    def __init__(self, name):
        self.name = name
        Sample.nObjects += 1

    def __del__(self):
        Sample.nObjects -= 1


# Instantiate 4 objects
oSample1 = Sample("A")
oSample2 = Sample("B")
oSample3 = Sample("C")
oSample4 = Sample("D")

# Delete 1 object
del oSample3

# See how many we have
print('There are', Sample.nObjects, 'Sample objects')
