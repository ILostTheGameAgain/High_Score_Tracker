
# High Score Tracker - Jackson / Alec / Tate
import pygame
from main_variables import * # Importing resoultion
pygame.display.set_mode(res)


# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker

import pygame



def main():
    res = 720,720
    screen = pygame.display.set_mode(res)
    white = (0,0,0)
    run = True
    while run:
        pygame.display.set_mode((width,height))
        pygame.display.set_caption("High Score Tracker")



        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                run = False
        if run:
            pygame.display.update()

            mouse = pygame.mouse.get_pos() # Stores mouse coordinates
        
main()

