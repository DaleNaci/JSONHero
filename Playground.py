import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg


import pylab

fig = pylab.figure(figsize=[4, 4], dpi=100, facecolor = (0.3, 0.3, 0.3))
ax = fig.gca()
ax.set_facecolor((0.3, 0.3, 0.3))
ax.bar([1, 2, 4], [3, 3, 3])

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()

import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 400), DOUBLEBUF)
screen = pygame.display.get_surface()

size = canvas.get_width_height()

surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
pygame.display.flip()

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
