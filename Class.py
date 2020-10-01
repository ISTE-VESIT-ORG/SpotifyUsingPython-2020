class MyNewClass:
    '''I have created a new class'''
    pass

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person()

# Output: <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)


# Calling object's greet() method
# Output: Hello
harry.greet()
#this translates later to
Person.greet(harry)