class Employee:
    def __init__(self,name,age,salary):
        print("Employee Created")
        self.name=name
        self.age=age
        self.salary=salary
    def DisplayInformation(self):
        print(f"Name of the employee is : {self.name}")
        print(f"Age of the employee is:{self.age}")
        print(f"Salary of the employee is: {self.salary}")

        def __del__(self):
            print("Employee Deleted")
emp1=Employee("Aneecka", 12, 10000000000000000000000000000000000000000)
emp2=Employee("Mimo",25, 250000000000000000000)
emp2.DisplayInformation()
emp2.DisplayInformation()
del emp1