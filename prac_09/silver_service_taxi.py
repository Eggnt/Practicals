from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def get_fare(self):
        """Return the price for the silver service taxi trip."""
        return self.price_per_km * self.current_fare_distance + self.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of {self.flagfall}"
