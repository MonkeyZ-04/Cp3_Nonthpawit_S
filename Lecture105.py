class Vehicle:
    licenseCode = ""
    serialNumber = ""
    def TurnonAirConditioner(self):
        print("Turn on : Air")
class Car(Vehicle):#สืบทอดแล้ว
    def sayHello(self):
        print("Hello world")
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

Car1 = Car()
Car1.TurnonAirConditioner()
Car1.sayHello()

Pickup1 = Pickup()
Pickup1.TurnonAirConditioner()

Van1 = Van()
Van1.TurnonAirConditioner()

Estatecar1 = Pickup()
Estatecar1.TurnonAirConditioner()

