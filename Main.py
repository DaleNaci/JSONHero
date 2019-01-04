import pygame, sys

import time
import json
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg

from pygame.locals import *

# JSON
file = open("SBHSData.json", "r").read()
jsonData = json.loads(file)

# Settings

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

screen = None


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

    bebasNeue = pygame.font.Font('Fonts/BebasNeue.ttf', 21)

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

        if framecount % random.choice([10, 15, 20]) == 0:
            newNote = Note(random.choice(jsonData), screen, bebasNeue)
            notes.append(newNote)
        framecount += 1

        for note in notes:
            note.draw()
            note.move()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # Checks each key
                threshold_lower = 440
                threshold_higher = 640
                for note in notes:
                    if threshold_lower < note.y:
                        if event.key == pygame.K_a and note.x == 0:
                            CNote.play()
                            notes.remove(note)
                        if event.key == pygame.K_s and note.x == 100:
                            DNote.play()
                            notes.remove(note)
                        if event.key == pygame.K_d and note.x == 200:
                            ENote.play()
                            notes.remove(note)
                        if event.key == pygame.K_f and note.x == 300:
                            FNote.play()
                            notes.remove(note)
                        if event.key == pygame.K_g and note.x == 400:
                            GNote.play()
                            notes.remove(note)
                        if event.key == pygame.K_h and note.x == 500:
                            ANote.play()
                            notes.remove(note)
                        if event.key == pygame.K_j and note.x == 600:
                            BNote.play()
                            notes.remove(note)
                        if event.key == pygame.K_k and note.x == 700:
                            HCNote.play()
                            notes.remove(note)
                for note in notes:
                    if note.y > threshold_higher:
                        notes.remove(note)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

class Note:
    def __init__(self, jsonObject, screen, font):
        self.screen = screen
        self.jsonObject = jsonObject
        self.font = font
        self.y = 0
        self.text = self.jsonObject["area"] + "," + self.jsonObject["version"] + "," + self.jsonObject["uptime"] + "," + self.jsonObject["hostname"]

        # Find x position and color based on area
        self.area = jsonObject["area"]
        if self.area == "storage":
            self.x = 0
            self.color = GRAY
        elif self.area == "bcloud":
            self.x = 100
            self.color = CYAN
        elif self.area == "prod":
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
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, 100, 100], 0)
        self.c = 0
        for self.value in self.text.split(","):
            self.textSurface = self.font.render(self.value, False, (255, 255, 255))
            self.screen.blit(self.textSurface, (self.x, self.y + self.c))
            self.c += 25

    def move(self):
        self.y += 15

main()
