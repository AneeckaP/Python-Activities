class Vehicle:
    def __init__(self, max_speed,mileage, name ):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
modelx=Vehicle(240,18,"Tesla ModelX")
bmwx7=Vehicle(300,5, "BMW X7")

print(modelx.name)
print(modelx.max_speed)
print(modelx.mileage)

print(bmwx7.name)
print(bmwx7.max_speed)
print(bmwx7.mileage)