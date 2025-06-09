class Vehicle:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
	def move(self):
		print("DRIVE")

class Car(Vehicle):
	pass

class Boat(Vehicle):
	def move(self):
		print("SAIL")
		
class Plane(Vehicle):
	def move(self):
		print("FLY")

car1 = Car("TATA", "Safari")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
	print(x.brand)
	print(x.model)
	x.move()