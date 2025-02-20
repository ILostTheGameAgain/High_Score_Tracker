# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker

import pygame



def main():
    width = 720
    height = 720
    run = True
    while run:
        pygame.display.set_mode((width,height))
        pygame.display.set_caption("DELTARUNE")



        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:

                width -= 1
                height -= 1
                if width == 1 or height == 1:
                    pygame.quit()
                    run = False
        if run:
            pygame.display.update()
main()
