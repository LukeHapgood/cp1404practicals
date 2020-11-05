from prac_08.car import Car
from random import uniform

class UnreliableCar(Car):
    """Specialised version of a Car that has added reliability"""

    def __init__(self, name, fuel, reliability):
        """ Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current reliability."""
        return "{}, fuel={}, odometer={}, reliability={}".format(self.name, self.fuel,
                                                 self.odometer, self.reliability)

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        Will not drive if reliability is lower than randomly generated number from 0-100
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