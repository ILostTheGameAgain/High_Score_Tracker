import pygame 
import random
from base_pygame import *
import sys


smallfont = pygame.font.SysFont('Arial',35) 
bigfont = pygame.font.SysFont('Arial',70) 




quit_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" : 400 ,"y" : 360}, # Top left is 0,0
"text": "Quit",
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100) ,
"text_offset": 0,
"text_color": (255,255,255)
}

menu_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" :  270,"y" : 630}, # Top left is 0,0
"text": "Menu", 
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100),
"text_offset": 0,
"text_color": (255,255,255)
}


def math_quiz():
    running = True
    while running: # Main Loop (break after quit)

        pygame.display.set_caption('Reaction Game')

        screen.fill((40,40,40)) # R G B (fills screen)

        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() # Stores mouse coordinates

        button(quit_button) # quit button creation
        button(menu_button) # reaction button creation

        screen.blit(bigfont.render('Reaction Game' , True , white),(100,60))

        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                running = False
                break
                
            if ev.type == pygame.MOUSEBUTTONDOWN: # Mouse Click Checking
                # This is where you find out where the button was clicking then run something depending on the button

                if quit_button['StartPos']['x'] <= mouse[0] <= quit_button['StartPos']['x']+quit_button['width'] and quit_button['StartPos']['y'] <= mouse[1] <= quit_button['StartPos']['y']+quit_button['height']: 
                    pygame.quit() 
                    running = False
                    break

                if reaction_button['StartPos']['x'] <= mouse[0] <= reaction_button['StartPos']['x']+reaction_button['width'] and reaction_button['StartPos']['y'] <= mouse[1] <= reaction_button['StartPos']['y']+reaction_button['height']: 
                    reaction_running = True
                    start_time = pygame.time.get_ticks()
                    react_time = random.randint(3000,6000)
                    stop = False
                    started = False # Checks if the green thing started or ended yet
                    pygame.display.set_caption('Click the thingy')
                    while reaction_running:

                        screen.fill((40,40,40))