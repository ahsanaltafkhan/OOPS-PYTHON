class Student:
    def __init__(self, name):
        self.name = name
class Department:
    def __init__(self, name, students):
        self.name = name
        self.students = students
students = [
    Student("Ahsan"),
    Student("Ali"),
    Student("Ahmed")
]
department = Department("Computer Science", students)
print(department.name)
for student in department.students:
    print(student.name)