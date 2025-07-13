from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def sound(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")
    def sound(self):
        print("Humans can generate variations of sound")
class Lion (Animal):
    def move(self):
        print("I can run")
    def sound(self):
        print("I can roar")

h=Human()
h.move()
h.sound()
l=Lion()
l.move()
l.sound()