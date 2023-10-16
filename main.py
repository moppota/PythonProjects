import deeznuts
import random
class Plane:
    def __init__(self, type, age):
        self.type = type
        self.age = age
    def __str__(self):
        return f"{self.type}({self.age})"

A320 = Plane("Airbus A320",0)

print(A320)
