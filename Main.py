import pygame, sys

import time
import json
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg

import pylab

from pygame.locals import *

# JSON
file = open("SBHSData.json", "r").read()
jsonData = json.loads(file)

# Settings

WINDOW_WIDTH = 800
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

    # "Successful" notes (Notes that the player hits) get stored here to be used on the graph
    success = []

    playing = True
    isGraphMade = False

    while True: # Main game loop

        if not isGraphMade:
            screen.fill(BLACK)

        # Create rectangle & segments on bottom of screen
        if playing:
            pygame.draw.rect(screen, WHITE, [0, WINDOW_HEIGHT - 100, 800, 100], 5)
            for i in range(1, 8):
                pygame.draw.line(screen, WHITE, [100 * i, WINDOW_HEIGHT - 100], [100 * i, 800], 5)
            if framecount % random.choice([15, 20, 25]) == 0:
                json = random.choice(jsonData)
                jsonData.remove(json)
                newNote = Note(json, screen, bebasNeue)
                notes.append(newNote)
            framecount += 1
            for note in notes:
                note.draw()
                note.move()
            threshold_higher = 570
            for note in notes:
                if note.y > threshold_higher:
                    notes.remove(note)

        if not playing and not isGraphMade:
            fig = pylab.figure(figsize=[8, 6], dpi=100, facecolor = (0.3, 0.3, 0.3))
            ax = fig.gca()
            ax.set_facecolor((0.3, 0.3, 0.3))
            areas = ["storage", "prod", "admin", "dev", "inet", "bcloud", "feed", "apex", "corp", "1", "tdmz", "null"]
            areaCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # areas and areaCounts are related by indexes

            # Loop through successes and find the area for each json object, and then sort it into areaCounts
            for json in success:
                a = json["area"]
                if a == "storage": areaCounts[0] += 1
                if a == "prod": areaCounts[1] += 1
                if a == "admin": areaCounts[2] += 1
                if a == "dev": areaCounts[3] += 1
                if a == "inet": areaCounts[4] += 1
                if a == "bcloud": areaCounts[5] += 1
                if a == "feed": areaCounts[6] += 1
                if a == "apex": areaCounts[7] += 1
                if a == "corp": areaCounts[8] += 1
                if a == "1": areaCounts[9] += 1
                if a == "tdmz": areaCounts[10] += 1
                if a == "": areaCounts[11] += 1

            ax.bar(areas, areaCounts)

            canvas = agg.FigureCanvasAgg(fig)
            canvas.draw()
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()

            size = canvas.get_width_height()

            surf = pygame.image.fromstring(raw_data, size, "RGB")
            screen.blit(surf, (0,0))

            isGraphMade = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and playing: # Checks each key
                threshold_lower = 440
                for note in notes:
                    if threshold_lower < note.y:
                        if event.key == pygame.K_a and note.x == 0:
                            CNote.play()
                            success.append(note.json)
                            notes.remove(note)
                        if event.key == pygame.K_s and note.x == 100:
                            DNote.play()
                            success.append(note.json)
                            notes.remove(note)
                        if event.key == pygame.K_d and note.x == 200:
                            ENote.play()
                            success.append(note.json)
                            notes.remove(note)
                        if event.key == pygame.K_f and note.x == 300:
                            FNote.play()
                            success.append(note.json)
                            notes.remove(note)
                        if event.key == pygame.K_g and note.x == 400:
                            GNote.play()
                            success.append(note.json)
                            notes.remove(note)
                        if event.key == pygame.K_h and note.x == 500:
                            ANote.play()
                            success.append(note.json)
                            notes.remove(note)
                        if event.key == pygame.K_j and note.x == 600:
                            BNote.play()
                            success.append(note.json)
                            notes.remove(note)
                        if event.key == pygame.K_k and note.x == 700:
                            HCNote.play()
                            success.append(note.json)
                            notes.remove(note)
                        if event.key == pygame.K_q:
                            playing = False
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
        self.json = jsonObject
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
