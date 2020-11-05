from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that has added reliability"""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """ Initialise an Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return "{}, plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = self.price_per_km * self.fanciness * self.current_fare_distance + self.flagfall
        return round(fare, 1)