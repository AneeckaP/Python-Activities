class Age:
    def __init__(self,a):
        self.age=a

    def __lt__(self,other):
        if(self.age < other.age):
            return "second person age is smaller"
        else:
            return "Second Person Age is bigger"
        
    def __eq__(self,other):
        if(self.age==other.age):
            return "same age"
        else:
            return "Different age"
        
Aneecka = Age(14)
Aadhya=Age(5)

print (Aneecka<Aadhya)
print (Aneecka==Aadhya)