class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
        pass
school_bus= Bus("school volvo", 180,12)
print("Vehicle Name: ", school_bus.name, "Speed:",school_bus.max_speed, "Mileage", school_bus.mileage)3