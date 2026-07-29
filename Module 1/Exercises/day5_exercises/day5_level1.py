class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def info(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, name, model, year, doors):
        super().__init__(name, model, year)
        self.doors = doors

    def honk(self):
        print("Beep Beep!")

car1=Car("Toyota","corolla",2035,4)
car1.info()
print("Doors:", car1.doors)
car1.honk()

class Motorcycle(Vehicle):
    def __init__(self, name, model, year, engine_cc):
        super().__init__(name, model, year)
        self.engine_cc = engine_cc

    def wheelie(self):
        print("The motorcycle is doing a wheelie!")

bike1 = Motorcycle("Yamaha", "R15", 2024, 155)

bike1.info()
print("Engine CC:", bike1.engine_cc)
bike1.wheelie()