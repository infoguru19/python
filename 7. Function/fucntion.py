def my_function():
    print("hello World")
my_function()

# Why we use function avoid repetation of code 
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Return
def greeting():
   return "Hello Good Morning"

message = greeting()
print(message)
print(greeting())  #Direct

