def add(*args):
    return sum(args)


print(add(3, 5))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(calculate(3, add=5, multiply=4))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", color="green", seats=6)
print(my_car.make)
print(my_car.color)
print(my_car.model)
