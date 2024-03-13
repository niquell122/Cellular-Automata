from copy import deepcopy
import numpy as np

default_wind = [
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0]
]

wind_dict = {
    'north_south_wind': np.array([
        [0.80, 1.90, 0.80],
        [0.50, 1.00, 0.50],
        [0.45, 0.75, 0.45]
    ]),
    'east_west_wind': np.array([
        [0.30, 0.40, 0.65],
        [0.55, 1.00, 2.00],
        [0.30, 0.40, 0.65]
    ]),
    'ne-sw-wind': np.array([
        [0.50, 0.80, 1.90],
        [0.45, 1.00, 0.80],
        [0.50, 0.45, 0.50]
    ]),
    'wasd': np.array([
        [0.85, 1.0, 0.85],
        [0.5, 1.0, 2.0],
        [0.5, 1.0, 2.0]
    ])
}

def get_wind(name, custom_wind=[], intensity=1):
    if(custom_wind==[]):
        wind = wind_dict[name]
        return wind * intensity
    else:
        return custom_wind * intensity


def neighborhood_fire(neighborhood, *args):
    
    new_neighborhood = deepcopy(neighborhood)
    print('neighborhood: \n' + str(neighborhood) + '\n')
    for arg in list(args):
        print('arg: \n' + str(arg) + '\n')
        apply_wind(new_neighborhood, arg)
    return new_neighborhood


def apply_wind(neighborhood, wind=default_wind, intensity=1):
    for i in range(3):
        neighborhood[i]=neighborhood[i] * wind[i] * intensity
    return neighborhood
