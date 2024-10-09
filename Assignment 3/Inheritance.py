#Single iinheritance 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

dog = Dog("Buddy")
#print(dog.speak()) 

#multiple inheritance

class Parent1:
    def greet(self):
        return "i am parent 1"

class Parent2:
    def introduce(self):
        return "i am parent 2"
    
class Child(Parent1, Parent2):
    def hello(self):
        return "i am the child"
    
c = Child()
'''print(c.greet())
print(c.introduce())
print(c.hello())

'''

#multilevel inheritance

class Car :
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
	def FullName(self):
		return f"{self.brand} {self.model}"
class ElectricCar(Car):
	def __init__(self, brand, model, battery):
		super().__init__(brand, model)
		self.battery = battery
e = ElectricCar("tesla", "Model S", "85kw")
print(e.model)
print(e.FullName())