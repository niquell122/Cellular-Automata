import random
from cellular_automata.cellular_automata import CellularAutomata
from math import floor
import numpy as np
from copy import deepcopy

from global_variables import map_side
from global_variables import empty_color
from global_variables import fire_color
from global_variables import forest_color
from global_variables import ash_color
from global_variables import catch_fire_chance

import cellular_automata.terrain as terrain
import cellular_automata.wind as wind

def fire(cells):
    total = 0
    for cell in cells:
        if cell == fire_color:
            total += 1
    return total


def ashes(cells):
    total = 0
    for cell in cells:
        if cell == ash_color:
            total += 1
    return total


def get_fire_index(neighborhood):
    return np.sum(neighborhood)
    

color_to_state={
    empty_color : 0,
    forest_color : 0,
    fire_color : 1,
    ash_color : 1
}


def serialize_neighborhood(neighborhood):
    arr = np.array(neighborhood)
    flat_arr = arr.reshape((1, -1))    
    new_neighborhood = flat_arr[0].reshape((3, 3))
    
    for row in range(3):
        for column in range(3):
            new_neighborhood[row][column] = color_to_state[neighborhood[row][column]]


n_s_wind = wind.get_wind('north_south_wind')

def wildfire_prob(home, neighborhood):
    ash_neighbors = ashes(neighborhood)
    
    new_neighborhood = serialize_neighborhood(neighborhood)
    new_neighborhood = wind.apply_wind(new_neighborhood, n_s_wind)
    ### applying new parameters go here
    
    fire_index = get_fire_index(new_neighborhood)
    
    if home == forest_color:
        chance = catch_fire_chance[fire_index]
        
        if random.random() < chance:
            return fire_color
        else:
            return forest_color

    if home == fire_color and fire_index > 7:
        return ash_color

    if home == fire_color and fire_index < ash_neighbors:
        return ash_color
    
    return home

arr = terrain.random_spread_in_the_center(40)

_2B = CellularAutomata(arr, wildfire_prob)
