class Student:
    university = "COMSATS"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_university(cls, university):
        cls.university = university
student1 = Student("Ahsan")
student2 = Student("Ali")
print(student1.university)
Student.change_university("NUST")
print(student1.university)
print(student2.university)