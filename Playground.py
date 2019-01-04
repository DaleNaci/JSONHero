import pygame, sys
import time
from pygame.locals import *

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)


# Counts out the number of objects in each storage
# maps = {}
# for s in j:
#     area = s["area"]
#     if area in map:
#         map[area] += 1
#     else:
#         map[area] = 1
#
# print(map)
