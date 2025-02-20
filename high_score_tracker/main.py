# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker

import pygame
import random



def main():
    width = 720
    height = 720
    keep_running = True
    while keep_running:
        pygame.display.set_mode((width,height))
        pygame.display.set_caption("e")

        

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
            
                width -= 20
                height -= 20

                if width <= 40:
                    pygame.quit()
                    keep_running = False

        if keep_running:
            pygame.display.update()
    

    


main()
