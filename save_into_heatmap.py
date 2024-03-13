import os
import pygame
from pygame.locals import *
import pylab
import time

import matplotlib.backends.backend_agg as agg
import matplotlib
matplotlib.use("Agg")

from global_variables import gen_text_color
from global_variables import text_rect_color

from cellular_automata.prototype_wind import _2B

prototype = "Wind - HeatMap Data"

current_time = time.time()
formatted_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(current_time))


current_dir = os.getcwd()
fileName = f"{prototype} {formatted_time}"
data_folder_path = os.path.join(current_dir, "data", "HeatMap")

window_width = 1200
window_height = 900
surface_width = 123

figsize_x = 12 # inches
figsize_y = 12 # inches

fig_dpi = 60 # pixels per inch

map_cord_x = window_width/2 - (figsize_x * fig_dpi)/2
map_cord_y = 50
map_cords = (map_cord_x, map_cord_y)

generation = 1
# savepoints = [1, 2, 3, 4, 5, 8, 10, 20, 30, 40]
# savepoints = list(range(41))
savepoints = [40]

def increase_generation():
    global generation
    generation += 1
    
def get_generation():
    global generation
    return generation


gen_text = "Gen"

def get_gen_text():
    global generation
    global gen_text
    return f"{gen_text}{generation}"

def save_data(surf):
    global generation
    global savepoints
    if generation in savepoints:
        print("Saving... " + get_gen_text())
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)
        image_path = os.path.join(data_folder_path, f"{fileName}.png")
        pygame.image.save(surf, image_path)

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 24)

window = (window_width, window_height)
screen = pygame.display.set_mode(window, DOUBLEBUF)
screen.fill((240,240,240))
screen = pygame.display.get_surface()

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

def update_screen():
    im.set_data(_2B.cells)
    canvas.draw()
    raw_data = renderer.tostring_rgb()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (map_cords))
    
    text_content = get_gen_text()
    text_surface = font.render(text_content, True, gen_text_color)

    text_rect = text_surface.get_rect()
    text_rect.center = (25,25)
    pygame.draw.rect(screen, text_rect_color, text_rect)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    save_data(surf)

def evolveOnce():
    increase_generation()
    _2B.evolve()
    # update_screen()

def verboseEvolve(n_steps):
    for i in range(n_steps):
        print(str(i+1))
        evolveOnce()

def fastEvolve(n_steps):
    for i in range(n_steps):
        increase_generation()
        _2B.evolve()

    update_screen()

def get_last_generation(imax=40):
    fastEvolve(imax-1)
    pygame.quit()

get_last_generation()