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
                pygame.quit()
                run = False
        if run:
            pygame.display.update()
        my_font = pygame.font.SysFont('Arial', 30)
        text_surface = my_font.render('Some Text', False, (0, 0, 0))
main()
