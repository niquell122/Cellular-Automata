import random
from cellular_automata.cellular_automata import CellularAutomata
from math import floor
import numpy as np
from copy import deepcopy

from global_variables import map_side
from global_variables import empty_color
from global_variables import fire_1_color
from global_variables import fire_2_color
from global_variables import fire_3_color
from global_variables import forest_color
from global_variables import ash_color
from global_variables import catch_fire_chance
from global_variables import RGB_to_int

import cellular_automata.map as map
import cellular_automata.wind as wind


def onFire(cell):
    if cell in [fire]:
        return True
    else: return False


def fire(cells):
    return count_color(cells, fire_1_color, fire_2_color, fire_3_color)


def ashes(cells):
    return count_color(cells, ash_color)


def count_color(neighborhood, *colors):
        n_color=0
        for i in range(np.size(neighborhood, axis=0)):
            for j in range(np.size(neighborhood, axis=1)):
                if(neighborhood[i][j] in list(colors)):
                    n_color+=1
        return n_color


def get_fire_index(neighborhood):
    return np.sum(neighborhood)


n_s_wind = wind.get_wind('north_south_wind')

def serialize_neighborhood(nbh):
    new_nbh = np.empty((3,3), dtype=int)
    for row in range(3):
        for cell in range(3):
            new_nbh[row][cell] = RGB_to_int(nbh[row][cell])
    return new_nbh



def wildfire_prob(home, neighborhood):
    ash_neighbors = ashes(neighborhood)
    fire_neighbors = fire(neighborhood)
    serialized_nbh = serialize_neighborhood(neighborhood)
    nbh_wind = wind.apply_wind(serialized_nbh, n_s_wind)
    
    fire_index = get_fire_index(nbh_wind)
    
    if home == forest_color:
        chance = catch_fire_chance[fire_index]
        
        if random.random() < chance:
            return fire_1_color
        else:
            return forest_color
    
    if home == fire_1_color:
            return fire_2_color

    if home == fire_2_color and fire_neighbors + ash_neighbors > 8:
        return fire_3_color
    
    if home == fire_3_color:
        return ash_color
    
    return home

arr = map.random_spread_in_the_center(40)

_2B = CellularAutomata(arr, wildfire_prob)
