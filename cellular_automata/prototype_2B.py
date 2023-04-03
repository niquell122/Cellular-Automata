import random
from cellular_automata.cellular_automata import CellularAutomata
from math import floor

side = 300
empty_color = (255,255,255)
fire_color = (240,45,45)
forest_color = (80,165,80)
ash_color = (30,30,30)

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
    if curr == forest_color and fire(neigh) > 1:
        return fire_color

    if curr == fire_color and fire(neigh) > 7:
        return ash_color

    if curr == fire_color and fire(neigh) < ashes(neigh):
        return ash_color

    return curr

arr = []

# proportion of fire agains forest
choices = [forest_color, forest_color, forest_color, forest_color, forest_color, forest_color, forest_color, fire_color] 

#### RANDOM MAP ####
# for i in range(side):
#     arr.append([])
#     for j in range(side):
#         arr[i].append(random.choice(choices))
#### RANDOM MAP ####

#### EMPTY MAP WITH RANDOM FIRE ON THE CENTER ####
for i in range(side):
    arr.append([])
    for j in range(side):
        arr[i].append(forest_color)
        
for i in range(floor(side/10)):
    for j in range(floor(side/10)):
        # arr[i+floor(side/2)][j+floor(side/2)] = 1
        arr[i+floor(side/2)][j+floor(side/2)] = random.choice(choices)

#### EMPTY MAP WITH FIRE ON THE CENTER ####

#### EMPTY MAP WITH FLAT AMMOUNT OF FIRE ON THE CENTER ####
# for i in range(side):
#     arr.append([])
#     for j in range(side):
#         arr[i].append(forest_color)
        
# for i in range(4):
#     for j in range(4):
#         arr[i+floor(side/2)][j+floor(side/2)] = fire_color
#### EMPTY MAP WITH FIRE ON THE CENTER ####


_2B = CellularAutomata(arr, wildfire)
