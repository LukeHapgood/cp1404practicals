from prac_08.car import Car
from random import uniform

class UnreliableCar(Car):
    """Specialised version of a Car that has added reliability"""

    def __init__(self, name, fuel, reliability):
        """ Initialise an UnreliableCar instance, based on parent class Car.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        reliability: a float between 0 and 100, that represents the percentage chance that the drive method will actually work
        """
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.odometer = 0

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        reliability_roll = uniform(0, 100)
        if self.reliability > reliability_roll:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            distance = 0
            print("Oh No! The car would not start.")
        return distance