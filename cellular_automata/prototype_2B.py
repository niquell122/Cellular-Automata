import random
from cellular_automata.cellular_automata import CellularAutomata
from math import floor

side = 300

def life(cells):
    total = 0
    for cell in cells:
        if cell == 0:
            total += 1
    return total


def fire(cells):
    total = 0
    for cell in cells:
        if cell == 1:
            total += 1
    return total


def ashes(cells):
    total = 0
    for cell in cells:
        if cell == 2:
            total += 1
    return total


def wildfire(curr, neigh):
    if curr == 0 and fire(neigh) > 1:
        return 1

    if curr == 1 and fire(neigh) > 7:
        return 2

    if curr == 1 and fire(neigh) < ashes(neigh):
        return 2

    return curr

arr = []
choices = [0, 0, 0, 0, 0, 0, 0, 1]  # proportion of fire (1) agains non-fire(0)

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
        arr[i].append(0)
        
for i in range(floor(side/10)):
    for j in range(floor(side/10)):
        # arr[i+floor(side/2)][j+floor(side/2)] = 1
        arr[i+floor(side/2)][j+floor(side/2)] = random.choice(choices)

#### EMPTY MAP WITH FIRE ON THE CENTER ####

#### EMPTY MAP WITH FLAT AMMOUNT OF FIRE ON THE CENTER ####
# for i in range(side):
#     arr.append([])
#     for j in range(side):
#         arr[i].append(0)
        
# for i in range(4):
#     for j in range(4):
#         arr[i+floor(side/2)][j+floor(side/2)] = 1
#### EMPTY MAP WITH FIRE ON THE CENTER ####



colors = ['white', 'red', 'black']
bounds = [0, 1, 2, 3]

_2B = CellularAutomata(arr, wildfire)
