class Teacher:
    def __init__(self, name):
        self.name = name
    def teach(self, student):
        print(f"{self.name} is teaching {student.name}.")
class Student:
    def __init__(self, name):
        self.name = name
teacher = Teacher("Dr. Ahmed")
student = Student("Ahsan")
teacher.teach(student)