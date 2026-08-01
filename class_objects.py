class student:
    name = "ahsan"

student1 = student()
student2 = student()
print(student1.name)
print(student2.name)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
p1 = person("ahsan", 20)
p2 = person("ali", 25)

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

