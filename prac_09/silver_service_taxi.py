"""
Prac 9
Silver Service Taxi Class
"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi that increase rate based on fanciness"""
    flagfall = 4.5
    def __init__(self,name,fuel,fanciness):
        """Initialise Silver Service Taxi, based on Taxi class"""
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string instance of Silver Service Taxi Class"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return of fare of the taxi trip plus the flagfall price"""
        fare = super().get_fare()
        return fare + self.flagfall


