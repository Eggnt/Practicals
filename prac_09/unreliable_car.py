from prac_06.car import Car
from random import uniform


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability > uniform(0, 100):
            distance_driven = 0
        else:
            distance_driven = super().drive(distance)
        return distance_driven
