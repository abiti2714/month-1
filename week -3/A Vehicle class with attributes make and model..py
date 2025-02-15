# A Vehicle class with attributes make and model.
class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def describe(self):
        return f"This is a Vehicle made by {self._make} with model {self._model}."

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self._num_doors = num_doors

    def describe(self):
        return f"This is a Car made by {self._make} with model {self._model} and has {self._num_doors} doors."

class Bike(Vehicle):
    _has_pedals = True

    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self._bike_type = bike_type

    def describe(self):
        return f"This is a Bike made by {self._make} with model {self._model} ({self._bike_type})."

def display_description(vehicle):
    print(vehicle.describe())

if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 4)
    bike = Bike("Trek", "Marlin 5", "Mountain Bike")

    display_description(car)
    display_description(bike)
    