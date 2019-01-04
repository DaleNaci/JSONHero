import pygame, sys
import time
import json
import random
from pygame.locals import *

# JSON
file = open("SBHSData.json", "r").read()
jsonData = json.loads(file)

# Settings

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600


# Colors
GRAY   = (100,100,100)
WHITE  = (255,255,255)
RED    = (255,  0,  0)
GREEN  = (  0,255,  0)
BLUE   = (  0,  0,255)
YELLOW = (255,255,  0)
ORANGE = (255,128,  0)
PURPLE = (255,  0,255)
CYAN   = (  0,255,255)
BLACK  = (  0,  0,  0)

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    arial = pygame.font.Font('Fonts/BebasNeue.ttf', 30)

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('JSON Hero')

    notes = []

    framecount = 0;

    while True: # Main game loop

        screen.fill(BLACK)

        file = open("SBHSData.json", "r").read()
        j = json.loads(file)

        if framecount % 60 == 0:
            newNote = Note(random.choice(jsonData))
            notes.append(newNote)
        framecount += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

class Note:
    def __init__(self, jsonObject):
        self.jsonObject = jsonObject
        y = 0
        text = self.jsonObject["area"] + "\n" + self.jsonObject["version"] + "\n" + self.jsonObject["uptime"] + "\n" + self.jsonObject["hostname"]

        # Find x position and color based on area
        self.area = jsonObject["area"]
        if self.area == "storage":
            self.x = 0
            self.color = GRAY
        elif self.area == "prod":
            self.x = 100
            self.color = WHITE
        elif self.area == "bcloud":
            self.x = 200
            self.color = RED
        elif self.area == "dev":
            self.x = 300
            self.color = GREEN
        elif self.area == "admin":
            self.x = 400
            self.color = BLUE
        elif self.area == "inet":
            self.x = 500
            self.color = YELLOW
        elif self.area == "feed":
            self.x = 600
            self.color = ORANGE
        else:
            self.x = 700
            self.color = PURPLE


    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, 100, 100], 0)
        textSurface = arial.render(self.text, False, (255, 255, 255))
        screen.blit(textsurface, (x + 5, y + 5))


main()


# import json
#
# file = open("SBHSData.json", "r").read()
# j = json.loads(file)
#
# # Counts out the number of objects in each storage
# map = {}
# for s in j:
#     area = s["area"]
#     if area in map:
#         map[area] += 1
#     else:
#         map[area] = 1
#     print(s)
#
# print(map)
