class Person:
    def __init__(self, name, idNumber):
        self.name=name
        self.idNumber=idNumber
    def display(self):
        print(self.name)
        print(self.idNumber)
class Employee(Person):
    def __init__(self,name,idNumber,salary,post):
        super().__init__(name,idNumber)
        self.salary=salary
        self.post=post
    def display(self):
        super().display()
        print(self.salary)
        print(self.post)
aneecka=Employee("Aneecka", 8184518, 200000, "Soft Dev")
aneecka.display()