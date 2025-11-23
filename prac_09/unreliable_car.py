"""
Prac 9
Unreliable Car Class
"""
from car import Car
from random import randint

class UnreliableCar(Car):
    """Car inheritance with a percentage chance to drive"""
    def __init__(self,name,fuel,reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return string instance of unreliable car"""
        return f"{super().__str__()}, Reliability = {self.reliability}%"

    def drive(self, distance):
        """Randomly drive car based on reliability"""
        drive_chance = randint(0,100)
        if drive_chance < self.reliability:
            super().drive(distance)
        else:
            distance = 0
        return distance
