# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker
import pygame
res = 720,720
screen = pygame.display.set_mode(res)
white = (0,0,0)
from base_pygame import button as btn
pygame.init()

white = (255,255,255) 
color_light = (170,170,170)
color_dark = (100,100,100) 



reaction_btn = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" :  270,"y" : 630}, # Top left is 0,0
"text": "Menu", 
"font": "Arial",
"fontsize": 35,
"hover_color": color_light,
"main_color": color_dark
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

