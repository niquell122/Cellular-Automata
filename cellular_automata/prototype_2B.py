import random
from cellular_automata.cellular_automata import CellularAutomata
from math import floor

from global_variables import side
from global_variables import empty_color
from global_variables import fire_color
from global_variables import forest_color
from global_variables import ash_color
from global_variables import catch_fire_chance

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


def wildfire(curr, neigh):
    fire_neighbors = fire(neigh)
    ash_neighbors = ashes(neigh)
    
    if curr == forest_color:
        chance = catch_fire_chance[fire_neighbors]
        
        if random.random() < chance:
            return fire_color
        else:
            return forest_color

    if curr == fire_color and fire_neighbors > 7:
        return ash_color

    if curr == fire_color and fire_neighbors < ash_neighbors:
        return ash_color

    return curr

arr = []

# proportion of fire agains forest
choices = [forest_color, forest_color, forest_color, forest_color, forest_color, forest_color, forest_color, fire_color] 


########################################  MAP Options  ########################################

#### RANDOM MAP ####
# for i in range(side):
#     arr.append([])
#     for j in range(side):
#         arr[i].append(random.choice(choices))
#### RANDOM MAP ####

#### FOREST MAP WITH RANDOM FIRE SPREAD IN THE CENTER ####
for i in range(side):
    arr.append([])
    for j in range(side):
        arr[i].append(forest_color)
        
fire_area = floor(side/10)
offset_map_center = floor(side/2 - fire_area/2)
        
for i in range(fire_area):
    for j in range(fire_area):
        arr[i+offset_map_center][j+offset_map_center] = random.choice(choices)
#### FOREST MAP WITH RANDOM FIRE SPREAD IN THE CENTER ####

#### FOREST MAP WITH FLAT AMMOUNT OF FIRE ON THE CENTER ####
# for i in range(side):
#     arr.append([])
#     for j in range(side):
#         arr[i].append(forest_color)
        
# for i in range(4):
#     for j in range(4):
#         arr[i+floor(side/2)][j+floor(side/2)] = fire_color
#### FOREST MAP WITH FIRE ON THE CENTER ####


_2B = CellularAutomata(arr, wildfire)
