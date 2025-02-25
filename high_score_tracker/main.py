<<<<<<< HEAD
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
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        my_font.render('Welcome to our game library', False, (0, 0, 0))
main()
=======
# High Score Tracker - Jackson / Alec / Tate
>>>>>>> 73b8b9d7d53552777b7892c96e887a9cc4314862
