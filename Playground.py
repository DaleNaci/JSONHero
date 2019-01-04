import pygame, sys
import time
from pygame.locals import *

def main():
    pygame.init()

    pygame.mixer.init()

    DISPLAYSURF = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Playground')

    CNote = pygame.mixer.Sound('sounds/notes/c.wav')
    DNote = pygame.mixer.Sound('sounds/notes/d.wav')
    ENote = pygame.mixer.Sound('sounds/notes/e.wav')
    FNote = pygame.mixer.Sound('sounds/notes/f.wav')
    GNote = pygame.mixer.Sound('sounds/notes/g.wav')
    ANote = pygame.mixer.Sound('sounds/notes/a.wav')
    BNote = pygame.mixer.Sound('sounds/notes/b.wav')
    HCNote = pygame.mixer.Sound('sounds/notes/high_c.wav')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
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
