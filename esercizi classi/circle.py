from math import *

class Circle:
    def __init__(self,radius):
        self.__radius = radius
    def SetRadius(self, radius):
        self.__radius = radius
    def GetRadius(self):
        return self.__radius
    def Area(self):
        return pi * self.__radius ** 2
    def __add__(self,AnotherCircle):
        return Circle(self.__radius + AnotherCircle.__radius)
    def __gt__ (self,AnotherCircle):
        return self.__radius > AnotherCircle.__radius
    def __lt__ (self,AnotherCircle):
        self.__radius < AnotherCircle.__radius
    def __str__(self):
        return "Circle with radius " + str(self.__radius)
