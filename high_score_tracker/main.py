# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker

import pygame
from file_functions import *
pygame.display.set_mode((720,720))

def main():
    width = 720
    height = 720
    run = True
    while run:
        pygame.display.set_mode((width,height))
        pygame.display.set_caption("DELTARUNE")



        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                run = False
        if run:
            pygame.display.update()
main()

