# import pygame
# from button import button

# pygame.init()

# #### Create a canvas on which to display everything ####
# window_width = 900
# window_height = 900
# window = (window_width, window_height)
# screen = pygame.display.set_mode(window)
# screen.fill((240,240,240))
# #### Create a canvas on which to display everything ####

# #### Create a surface for the forest map ####
# surface_width = 512
# surface_height = 512
# surface = (surface_width,surface_height)
# map = pygame.Surface(surface)
# #### Create a surface for the forest map  ####

# #### Populate the surface with objects to be displayed ####
# pygame.draw.rect(map,(0,255,255),(200,200,40,40))
# pygame.draw.rect(map,(255,0,255),(120,120,50,50))
# #### Populate the surface with objects to be displayed ####

# #### Blit the surface onto the canvas ####
# screen_center_for_map = (window_width/2 - surface_width/2, 50)
# screen.blit(map, screen_center_for_map)
# #### Blit the surface onto the canvas ####


# #### Create a button ####
# btn_width = 50
# btn_height = 50
# btn_pos_x = window_width/2
# btn_pos_y = window_width/2 + surface_width/2
# btn_color = (0,255,0)
# btn = button(btn_color, (btn_pos_x, btn_pos_y), btn_width, btn_height)
# #### Create a button ####

# #### Blit the button onto the canvas ####
# btn.draw(screen)
# #### Blit the button onto the canvas ####

# #### Update all the elements in the window ####
# def update_window():
    
#     screen.blit(map, screen_center_for_map)
#     btn.draw(screen, (0,0,0))
# #### Update all the elements in the window ####

# #### Update the the display and wait ####
# pygame.display.flip()
# done = False
# while not done:
#     update_window()
#     pygame.display.update()
    
#     for event in pygame.event.get():
#         pos = pygame.mouse.get_pos()
        
#         if event.type == pygame.QUIT:
#             done = True
        
#         btn.handle(event, pos)
# #### Update the the display and wait ####

# pygame.quit()
