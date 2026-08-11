
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "ACcord")
print(car1.brand)
print(car1.model)
print(car2.brand)
print(car2.model)
car1.model = "TUCSON"
print(car1.model)