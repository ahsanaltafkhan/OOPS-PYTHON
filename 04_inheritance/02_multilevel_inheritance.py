class Grandparent:
    def house(self):
        print("Grandparent owns a house.")
class Parent(Grandparent):
    def car(self):
        print("Parent owns a car.")
class Child(Parent):
    def laptop(self):
        print("Child owns a laptop.")

child = Child()
child.house()
child.car()
child.laptop()