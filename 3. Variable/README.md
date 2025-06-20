# Variable
Variables are containers for storing data values.
```
x = 10
y = "Ravi"
print(x)
print(y)
```
## Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
### Legal Variable names
```
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```
### Variable names are case-sensitive.
```
a = 4
A = "Sally"
#A will not overwrite a
```
### Many Values to Multiple Variables
```
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
### One Value to Multiple Variables
```
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

## Variables do not need to be declared with any particular type, and can even change type after they have been set.
```
x = 10      # x is of type int
x = "Ravi" # x is now of type str
print(x)
```

# Casting
If we want to specify the datatype of a variable, this can be done with casting.
```
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

# Get the Type
You can get the data type of a variable with the type() function.
```
x = 5
y = "John"
print(type(x))  # Display datatype of x: Integer
print(type(y))  # Display datatype of x: String
````

# Single or Double Quotes
String variables can be declared either by using single or double quotes:
```
x = "John" # Both are the same
x = 'John'
```

# Output Variables
The Python print() function is often used to output variables.
```
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```


