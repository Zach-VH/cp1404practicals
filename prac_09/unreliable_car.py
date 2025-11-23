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

    def drive(self, distance):
        drive_chance = randint(0,100)
        if drive_chance < self.reliability:
            super().drive(distance)
