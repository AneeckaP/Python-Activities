class Parent:
    def car(self):
        print("This is parent's car")
class Child(Parent):
    def car(self):
        print("This is Child's car")

c=Child()
c.car=()
p=Parent()
p.car()