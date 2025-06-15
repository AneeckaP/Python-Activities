class Parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age
blue=Parrot("Blue",10)
woo=Parrot("Woo",15)
           
print(f"Blue is a {blue.species}")
print(f"Woo is also a {woo.species}")

print(f"{blue.name} is {blue.age} years")
print(f"{woo.name} is {woo.age} years")