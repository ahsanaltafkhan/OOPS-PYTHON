class Student:
    def __init__(self, name):
        self.name = name
student = Student("Ahsan")
print(student.name)
student.name = "Ali"
print(student.name)