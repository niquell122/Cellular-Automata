import pygame
from pygame.locals import *
import pylab
from time import sleep

import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import animation
matplotlib.use("Agg")

from cellular_automata.prototype_2B import _2B

window_width = 900
window_height = 900
surface_width = 123

figsize_x = 5 # inches
figsize_y = 5 # inches

fig_dpi = 100 # pixels per inch

map_cord_x = window_width/2 - (figsize_x * fig_dpi)/2
map_cord_y = 50
map_cords = (map_cord_x, map_cord_y)

#### PYGAME INIT ####

pygame.init()

window = (window_width, window_height)
screen = pygame.display.set_mode(window, DOUBLEBUF)
screen.fill((240,240,240))
screen = pygame.display.get_surface()
#### PYGAME INIT ####


#### PLOT MATRIX ####
fig = pylab.figure(figsize=[figsize_x, figsize_y], # Inches
                    dpi=fig_dpi,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                    )
ax = fig.gca()
im = ax.matshow(_2B.cells)

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()
size = canvas.get_width_height()
surf = pygame.image.fromstring(raw_data, size, "RGB")

screen.blit(surf, (map_cords))
pygame.display.flip()

#### PLOT MATRIX ####

def update_screen():
    im.set_data(_2B.cells)
    canvas.draw()
    raw_data = renderer.tostring_rgb()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (map_cords))
    pygame.display.flip()


def evolveOnce():
    _2B.evolve()
    sleep(0.2)
    update_screen()

def verboseEvolve(n_steps):
    for i in range(n_steps):
        print(str(i+1))
        evolveOnce()

def fastEvolve(n_steps):
    for i in range(n_steps):
        _2B.evolve()
    sleep(0.2)
    update_screen()

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     evolveOnce()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                evolveOnce()
            if event.key == pygame.K_f:
                fastEvolve(10)
            if event.key == pygame.K_v:
                verboseEvolve(10)
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_u:
                update_screen()