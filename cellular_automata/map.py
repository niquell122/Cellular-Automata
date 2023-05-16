from math import floor
import random

from global_variables import map_side
from global_variables import empty_color
from global_variables import fire_color
from global_variables import forest_color
from global_variables import ash_color
from global_variables import catch_fire_chance


def single_staring_point(size):
    arr = []
    for i in range(map_side):
        arr.append([])
        for j in range(map_side):
            arr[i].append(forest_color)
        
    for i in range(size):
        for j in range(size):
            arr[i+floor(map_side/2)][j+floor(map_side/2)] = fire_color
    
    return arr


def random_spread_in_the_center(size):
    arr = []
    choices = [forest_color, forest_color, forest_color, forest_color, fire_color] 

    for i in range(map_side):
        arr.append([])
        for j in range(map_side):
            arr[i].append(forest_color)
            
    fire_area = floor(map_side/10)
    offset_map_center = floor(map_side/2 - fire_area/2)
            
    for i in range(fire_area):
        for j in range(fire_area):
            arr[i+offset_map_center][j+offset_map_center] = random.choice(choices)
    
    return arr
    