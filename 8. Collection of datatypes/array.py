def list_cars(my_cars):
  for i in my_cars:
    print(i)
  
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars[0])

list_cars(cars)
