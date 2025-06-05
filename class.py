class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #  __str__() Function: function controls what should be returned when the class object is represented as a string.
    def __str__(self):
        return f"{self.name} {self.age}"
    # Object Methods: Methods in objects are functions that belong to the object.    
    def myfun(self):
        print("Hello My name is " + self.name )
    # self Parameter : It has to be the first parameter of any function in the class  
    def paramFun(abc):
        print("Hello My name is " + abc.name)
        
p1 = person("ravi", 32)
print(p1)
p1.myfun()
p1.paramFun()

# Modify Object Properties
p1.age = 30
print(p1)

# Delete Objects
del p1
print(p1) # ERROR: NameError: name 'p1' is not defined

# pass Statement: class definitions cannot be empty, but if you for some reason have a class definition with no content, 
# Put in the pass statement to avoid getting an error.
class Child:
    pass