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

arial = pygame.font.SysFont('Arial', 30)


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

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('JSON Hero')

    # Playable sound for each note of octave (C Major)
    CNote = pygame.mixer.Sound('sounds/notes/c.wav')
    DNote = pygame.mixer.Sound('sounds/notes/d.wav')
    ENote = pygame.mixer.Sound('sounds/notes/e.wav')
    FNote = pygame.mixer.Sound('sounds/notes/f.wav')
    GNote = pygame.mixer.Sound('sounds/notes/g.wav')
    ANote = pygame.mixer.Sound('sounds/notes/a.wav')
    BNote = pygame.mixer.Sound('sounds/notes/b.wav')
    HCNote = pygame.mixer.Sound('sounds/notes/high_c.wav')

    # box_X = 0
    # box_Y = 0

    framecount = 0

    notes = []

    while True: # Main game loop

        screen.fill(BLACK)

        # Create rectangle & segments on bottom of screen
        pygame.draw.rect(screen, WHITE, [0, WINDOW_HEIGHT - 100, 800, 100], 5)
        for i in range(1, 8):
            pygame.draw.line(screen, WHITE, [100*i, WINDOW_HEIGHT - 100], [100*i, 800], 5)

        # pygame.draw.rect(screen, GRAY, [box_X, box_Y, 100, 100], 0)
        # box_Y += 1

        if (framecount % 60 == 0):
            notes.add(Note(random.choice(list(jsonData.keys()))))



        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # Checks each key
                if event.key == pygame.K_a:
                    CNote.play()
                if event.key == pygame.K_s:
                    DNote.play()
                if event.key == pygame.K_d:
                    ENote.play()
                if event.key == pygame.K_f:
                    FNote.play()
                if event.key == pygame.K_g:
                    GNote.play()
                if event.key == pygame.K_h:
                    ANote.play()
                if event.key == pygame.K_j:
                    BNote.play()
                if event.key == pygame.K_k:
                    HCNote.play()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

class Note:
    def __init__(self, jsonObject):
        self.jsonObject = jsonObject
        y = 0
        text = jsonObject["area"] + "\n" + jsonObject["version"] + "\n" + jsonObject["uptime"] + "\n" + jsonObject["hostname"]
        # Find x position and color based on area
        self.area = jsonObject["area"]
        if area == "storage":
            self.x = 0
            self.color = GRAY
        elif area == "prod":
            self.x = 100
            self.color = WHITE
        elif area == "bcloud":
            self.x = 200
            self.color = RED
        elif area == "dev":
            self.x = 300
            self.color = GREEN
        elif area == "admin":
            self.x = 400
            self.color = BLUE
        elif area == "inet":
            self.x = 500
            self.color = YELLOW
        elif area == "feed":
            self.x = 600
            self.color = ORANGE
        else:
            self.x = 700
            self.color = PURPLE


    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, 100, 100], 0)
        textSurface = arial.render(self.text, False, (0, 0, 0))
        screen.blit(textsurface, (x + 5, y + 5))


main()
