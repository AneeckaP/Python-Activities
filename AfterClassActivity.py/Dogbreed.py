class Dog:
    species = "Canine"  

    def __init__(self, name, breed):
        self.name = name  
        self.breed = breed 

    def display_details(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")



dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Beagle")


dog1.display_details()
dog2.display_details()