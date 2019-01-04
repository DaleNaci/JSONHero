import pygame, sys
import time
import json
from pygame.locals import *

f = open("SBHSData.json", "r").read()
j = json.loads(f)

# Settings

WINDOW_WIDTH = 800
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

def main():
    pygame.init()

    pygame.mixer.init()

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

    box_X = 0
    box_Y = 0

    while True: # Main game loop

        # Create rectangle & segments on bottom of screen
        pygame.draw.rect(screen, WHITE, [0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 100], 5)
        for i in range(1, 8):
            pygame.draw.line(screen, WHITE, [100*i, WINDOW_HEIGHT - 100], [100*i, WINDOW_HEIGHT], 5)

        pygame.draw.rect(screen, GRAY, [box_X, box_Y, 100, 100], 0)
        box_X += 1
        box_Y += 1

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

main()
