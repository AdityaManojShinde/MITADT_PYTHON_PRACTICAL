class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bycycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

car = Car()
bycycle = Bycycle()

car.move()
bycycle.move()