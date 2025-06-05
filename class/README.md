# Python Classes/Objects
Python is an object oriented programming language.
**Almost everything in Python is an object, with its properties and methods.**
**A Class is like an object constructor, or a "blueprint" for creating objects.**

## __init__() Function
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
```
## __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.
```
  def __str__(self):
    return f"{self.name}({self.age})"
```
## Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.
```
  def myfunc(self):
    print("Hello my name is " + self.name)
```
## self Parameter
The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
It does not have to be named `self`, you can call it whatever you like, but it has to be the first parameter of any function in the class:\
**Use the words mysillyobject and abc instead of self:**
```
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
```