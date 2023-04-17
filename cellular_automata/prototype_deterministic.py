import random
from cellular_automata.cellular_automata import CellularAutomata
from math import floor

from global_variables import map_side
from global_variables import empty_color
from global_variables import fire_color
from global_variables import forest_color
from global_variables import ash_color
from global_variables import catch_fire_chance

import cellular_automata.terrain as terrain

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


def wildfire_deterministic(curr, neigh):
    fire_neighbors = fire(neigh)
    ash_neighbors = ashes(neigh)
    
    ### combinando caracteristicas de diversos modelos
    if curr == forest_color:
        
        if fire_neighbors > 2:
            return fire_color
        else:
            return forest_color

    if curr == fire_color and fire_neighbors > 7:
        return ash_color

    if curr == fire_color and fire_neighbors < ash_neighbors:
        return ash_color
    ### o fogo apaga em função do tempo. parâmetro _tempo_de_queima_
    ### reignição
    ### matriz de influencia do vento
    return curr

arr = terrain.random_spread_in_the_center(40)

_2B = CellularAutomata(arr, wildfire_deterministic)
