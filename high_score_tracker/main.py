# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker
import pygame
from file_functions import *
from reaction_time_game import *
from base_pygame import *

quit_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" : 550 ,"y" : 650}, # Top left is 0,0
"text": "Quit",
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100) ,
"text_offset": 35,
"text_color": (255,255,255)
}

pygame.display.set_mode((720,720))

def main():
    run = True
    while run:

        mouse = pygame.mouse.get_pos()

        button(quit_button)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                run = False

            if ev.type == pygame.MOUSEBUTTONDOWN: # Mouse Click Checking

                if quit_button['StartPos']['x'] <= mouse[0] <= quit_button['StartPos']['x']+quit_button['width'] and quit_button['StartPos']['y'] <= mouse[1] <= quit_button['StartPos']['y']+quit_button['height']: # Checking in this range for clicking the button
                    pygame.quit() 
                    running = False
                    break

        if run:
            pygame.display.update()
        button(quit_button)
main()

