square_size = 1                 # meter
map_side = 150                  # array dimensions


#### Cell Colors
empty_color = (255,255,255)     # RGB black
fire_color = (240,45,45)        # RGB red
forest_color = (80,165,80)      # RGB green
ash_color = (30,30,30)          # RGB gray


#### CHANCE TO CATCH FIRE BASED ON THE NUMBER OF BURNING NEIGHBORS ####
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
### ao aplicar a matriz do vento estes valores se tornam o coeficiente de "catch_fire" mas funcionam da mesma maneira (mudar valores%)
### dict coef:chance