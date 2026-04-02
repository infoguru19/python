a = 33
b = 200
if b > a:
  print(f"{b} is greater than {a}")
  print("b is greater")
  
# Checking if number is positive or not
a = 10
if a > 0:
    print(f"{a} is positive number")
    
# Using variable in condition
log_in = False
if log_in:
    print("Welcome Back !")
   
 
#else if
a = 300
b = 200
if b > a:
  print(f"{b} is greater than {a}")
elif a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")

# Else
a = 300
b = 200
if b > a:
  print(f"{b} is greater than {a}")
elif a == b:
    print(f"{b} is equal to {a}")
else: 
    print(f"{b} is less than {a}")
    
# Challenge
"""
1. Create a variable age with the value 20
2. Write an if statement that prints "Child" if age is less than 13
3. Add an elif that prints "Teenager" if age is less than 18
4. Add an else that prints "Adult
""""
#Solution

# Create age variable
age = 20
# Write if/elif/else
if age < 13:
  print("Child")
elif age < 18:
  print("Teenager")
else:
  print("Adult")

