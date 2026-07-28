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