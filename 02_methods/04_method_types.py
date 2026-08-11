class Student:
    university = "COMSATS"
    def __init__(self, name):
        self.name = name
    def instance_method(self):
        print(f"Student: {self.name}")
    @classmethod
    def class_method(cls):
        print(f"University: {cls.university}")
    @staticmethod
    def static_method():
        print("This is a static method.")
student = Student("Ahsan")
student.instance_method()
Student.class_method()
Student.static_method()