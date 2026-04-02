# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
# Looping through string
x = "banana"
for i in x:
    print(i)
    
# Loop with break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
      break

# To loop through a set of code a specified number of times, we can use the range() function
for i in range(6):
    print(i)
for  i in range(1,6):
    print(i)
for i in range(2,20,4):  # Increment seq with 4
    print(i)
