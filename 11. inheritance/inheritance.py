# Parent class
class Person:
    def __init__(self,first, last):
        self.firstname = first
        self.lastname = last
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Ravi", "Ranjan")
x.printname()

# Child class
class Student(Person):
    def __init__(self, first, last, year):
        super().__init__(first, last)       # Super function to call the constructor of the parent class
        self.graduationYear = year          # Adding Property to the child class

    def welcome(self):                      # Adding method to the child class
        print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationYear)

y = Student("John", "Doe", 2023)
y.printname()
print(y.graduationYear)
y.welcome()  # Calling the method from the child class