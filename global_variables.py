square_size = 1                 # meter
map_side = 100                  # array dimensions



gen_text_color = (0, 0, 0)      # black 
text_rect_color = (255,255,255) # white

#### Cell Colors

empty_color = (255,255,255)     # RGB black
forest_color = (80,165,80)      # RGB green

fire_color = (255,30,0)         # RGB bright red
fire_1_color = (255,105,0)      # RGB orange
fire_2_color = (255,30,0)       # RGB bright red
fire_3_color = (150,20,20)        # RGB dark red

ash_color = (30,30,30)          # RGB gray


catch_fire_chance = {
    0: 0,
    1: 0.2,
    2: 0.4,
    3: 0.6,
    4: 0.8,
    5: 1,
    6: 1,
    7: 1,
    8: 1
}


RBG_int_dict = {
    empty_color : 0,
    forest_color : 0,
    fire_color: 1,
    fire_1_color : 0.9,
    fire_2_color : 1.1,
    fire_3_color : 0.8,
    ash_color : 0
}
RBG_int_dict


def RGB_to_int(RGB):
    return RBG_int_dict.get(RGB, -1)