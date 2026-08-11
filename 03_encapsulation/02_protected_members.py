class Student:
    def __init__(self, name):
        self._name = name
class UniversityStudent(Student):
    def display(self):
        print(self._name)
student = UniversityStudent("Ahsan")
student.display()