CURRENT_YEAR = 2022
LIMIT_YEAR = 50
class Guitar:
    """create the object of guitar included name year cost"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """display a sentence about the introduction of guitar"""
        return f"{self.name}({self.year}: ${self.cost})"

    def get_age(self):
        """calculate the age of each guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """determine the age of guitar whether it is more than 50 years"""
        return self.get_age() >= LIMIT_YEAR




guitar = Guitar()
