day = 3
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    
    
#Challenge
"""
1. Create a variable day with the value 3
2. Use a match statement to check the value of day
3. Add a case 3 that prints "Wednesday"
4. Add a wildcard case _ that prints "Other day
"""

#Solution

# Create variable day
day = 3
# Use match statement
match day:
  case 3:
    print("Wednesday")
  case _:
    print("Other day")
