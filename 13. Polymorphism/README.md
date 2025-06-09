# Polymorphism

The word `polymorphism` means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

## Function Polymorphism
Python function that can be used on different objects is the len() function.

### String
```
x = "Hello World!"
print(len(x))       #OUTPUT: 12
```
### Tuple
```
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))                        #OUTPUT: 3 
```
### Dictionary
```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))                #OUTPUT 3
````

## Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
For example, we have three classes: `Car`, `Boat`, and `Plane`, and they all have a method called `move()`.

## Inheritance Class Polymorphism
we can make a parent class called `Vehicle`, and make `Car`, `Boat`, `Plane` child classes of Vehicle, the child classes inherits the Vehicle methods, but can override.


