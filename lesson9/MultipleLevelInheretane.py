class Vehicle;
    def __init__(self, make, model, year)
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print(f"make: {self.make}, model:{self.model} ,Year:{self.year}")

class Car(Vehicle):
    def __init__(self, make , model, body_style):
        super().__init__(make,model,year)
        self.body_style=body_style

class ElecticCar(Car):
    def __init__(self, make, model, year, body_style, batery_capacity):
        super().__init__(make, model,year,body_style)
        self.batery_capacity=batery_capacity

    def charge(self):
        print(f"Charging the electric car.")

tesla= ElectricCar("Tesla","cybertruck", 20223 ,"trianguler", 112.4)
print(tesla.charge)