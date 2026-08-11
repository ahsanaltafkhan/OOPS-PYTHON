class Student:
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
student1 = Student("Ahsan", 20, "BSCS")
student2 = Student("Ali", 21, "BSSE")
print(student1.name)
print(student1.age)
print(student1.degree)
print(student2.name)
print(student2.age)
print(student2.degree)