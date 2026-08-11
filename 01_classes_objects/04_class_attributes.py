class Student:
    university = "COMSATS University Islamabad"
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
student1 = Student("Ahsan", "BSCS")
student2 = Student("Ashhad", "BSAI")
print(student1.name)
print(student1.university)
print(student2.name)
print(student2.university)
Student.university = "AIR           "
print(student1.university)
print(student2.university)