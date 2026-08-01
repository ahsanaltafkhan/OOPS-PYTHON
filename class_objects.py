class student:
    name = "ahsan"

student1 = student()
student2 = student()
print(student1.name)
print(student2.name)
class Person:
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree

p1 = Person("Ahsan", 20, "BSCS")
p2 = Person("Ali", 25, "BSSE")

print(p1.name)
print(p1.age)
print(p1.degree)

print()

print(p2.name)
print(p2.age)
print(p2.degree)

class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = car("Toyota", "Camry")
c2 = car("Honda", "Civic")

class animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

n1 = animal("Dog", "Bark")
n2 = animal("Cat", "Meow")

#passing object as parameter
class school:
    def __init__(self, name, student):
        self.name = name
        self.student = student  

