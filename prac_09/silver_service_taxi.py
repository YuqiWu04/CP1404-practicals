from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """sliver service class content"""
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """the initial value from parent class and add some new parameter"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """return a string which is about some specific data of sliver service taxi"""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """get the final cost at the end of trip"""
        return super().get_fare() + self.flagfall


