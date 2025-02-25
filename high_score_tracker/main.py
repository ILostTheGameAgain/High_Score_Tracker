# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker
import pygame
res = 720,720
screen = pygame.display.set_mode(res)
white = (0,0,0)
from base_pygame import button as btn

reaction_btn = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" :  270,"y" : 630}, # Top left is 0,0
"text": "Menu", 
"font": "Arial",
"fontsize": 35,
"hover_color": (80,80,80),
"main_color": (40,40,40),
"text_offset": 0
}


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
        btn(reaction_btn)
main()

