# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker

import pygame
from file_functions import *
pygame.display.set_mode((720,720))

def main():
    run = True
    while run:
        pygame.display.set_caption("Menu")



        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                run = False

        if run:
            pygame.display.update()


main()

