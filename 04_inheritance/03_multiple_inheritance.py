class Father:
    def skills(self):
        print("Father: Business")
class Mother:
    def talent(self):
        print("Mother: Art")
class Child(Father, Mother):
    pass
child = Child()
child.skills()
child.talent()