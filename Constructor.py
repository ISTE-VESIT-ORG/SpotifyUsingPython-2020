

class Person:
    
    """
    This is a Person
    Person has attributes : age , gender, name
    """

    def __init__(self,name,age,gender):
        '''
        All variables here declared are called as instance varibles
        '''
        self.name = name
        self.age = age
        self.gender = gender

        #instance method
    def print_Person_Details(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)


p1 = Person("Aditya",20,"M")
p2 = Person("Akash",21,"M")
Person.print_Person_Details(p1)
