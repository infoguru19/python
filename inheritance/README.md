# Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
**Parent class** is the class being inherited from, also called base class.
**Child class** is the class that inherits from another class, also called derived class.

## Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).
**Note:** The __init__() function is called automatically every time the class is being used to create a new object.

### Add the __init__() function to the Student class:
```
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
```
***Note:*** The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
Example
```
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```

## super() Function
Python also has a `super()` function that will make the child class inherit all the methods and properties from its parent:
```
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```

## Add Properties
Add a property called graduationyear to the Student class:
```
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
```

## Add Methods
Add a method called welcome to the Student class:
```
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
```