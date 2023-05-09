import random
from cellular_automata.cellular_automata import CellularAutomata
from math import floor

from global_variables import map_side
from global_variables import empty_color
from global_variables import fire_color
from global_variables import forest_color
from global_variables import ash_color
from global_variables import catch_fire_chance
import numpy as np

import cellular_automata.terrain as terrain

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

def wildfire_prob(home, neigh):
    fire_neighbors = fire(neigh)
    ash_neighbors = ashes(neigh)
    
    ### combinando caracteristicas de diversos modelos
    if home == forest_color:
        chance = catch_fire_chance[fire_neighbors]
        
        if random.random() < chance:
            return fire_color
        else:
            return forest_color

    if home == fire_color and fire_neighbors > 7:
        return ash_color

    if home == fire_color and fire_neighbors < ash_neighbors:
        return ash_color
    ### o fogo apaga em função do tempo. parâmetro _tempo_de_queima_
    ### reignição
    ### matriz de influencia do vento
    return home

arr = terrain.random_spread_in_the_center(40)

_2B = CellularAutomata(arr, wildfire_prob)
