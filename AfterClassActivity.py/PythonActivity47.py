#Abstraction: A method where a parent defines a function as abstract method and makes it mandatory for the child to override the method.
from abc import ABC, abstractmethod

class ParentClass(ABC):
    def print_var(self,x):

        print("Passed Value:",x)

    @abstractmethod
    def task(self):
        print("We are inside parent's task")

class ChildClass(ParentClass):
    def task(self):
        print("Okay I did this now")

obj1=ChildClass()
obj1.print_var(12)