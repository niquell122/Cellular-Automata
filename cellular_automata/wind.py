from copy import deepcopy
import numpy as np

default_wind = [
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0]
]

wind_dict = {
    'north_south_wind': [
        [2.0, 2.0, 2.0],
        [1.0, 1.0, 1.0],
        [0.5, 0.5, 0.5]
    ],

    'east_west_wind': [
        [0.5, 1.0, 2.0],
        [0.5, 1.0, 2.0],
        [0.5, 1.0, 2.0]
    ]
}
# wind_dict.setdefault(default_wind)

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


def apply_wind(neighborhood, wind, intensity=1):
    for i in range(3):
        for j in range(3):
            neighborhood[i][j]=neighborhood[i][j] * wind[i][j] * intensity
    return neighborhood