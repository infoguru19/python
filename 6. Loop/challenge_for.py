"""
1. Create a list called fruits with: "apple", "banana", "cherry"
2. Write a for loop that prints each item in fruits
3. Use break to stop the loop when the item is "banana"
"""

# Create the fruits list
fruits = ["apple", "banana", "cherry"]
# Loop through fruits, break at "banana"
for x in fruits:
  print(x)
  if x == "banana":
    break
