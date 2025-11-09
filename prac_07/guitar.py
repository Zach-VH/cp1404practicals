"""
Guitar class - Creates a guitar class instance

Time to complete both guitar and guitar test
Estimated: 15 minutes
Actual: 12 minutes 21 seconds
"""
from datetime import date

current_year = date.today().year


class Guitar:
    """A representation of a guitar object"""
    def __init__(self, name="",year=0,cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return current_year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False