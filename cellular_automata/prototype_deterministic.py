import random
from cellular_automata.cellular_automata import CellularAutomata
from math import floor
import numpy as np

from global_variables import fire_color
from global_variables import forest_color
from global_variables import ash_color

import cellular_automata.map as map

def fire(cells):
    return count_color(cells, fire_color)


def ashes(cells):
    return count_color(cells, ash_color)


def count_color(neighborhood, color):
        n_color=0
        for i in range(np.size(neighborhood, axis=0)):
            for j in range(np.size(neighborhood, axis=1)):
                if(neighborhood[i][j] == color):
                    n_color+=1
        return n_color


def wildfire_deterministic(home, neigh):
    fire_neighbors = fire(neigh)
    ash_neighbors = ashes(neigh)
    if home == forest_color:
        if fire_neighbors > 2:
            return fire_color
        else:
            return forest_color
    if home == fire_color and fire_neighbors + ash_neighbors == 9:
        return ash_color
    return home

arr = map.random_spread_in_the_center(40)

_2B = CellularAutomata(arr, wildfire_deterministic)
