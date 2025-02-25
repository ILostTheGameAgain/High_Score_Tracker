#Alec George Memory Game

#will create a random string of letters and numbers and let the user rewrite it when they no longer see it. If they get it correct, it gets longer

import pygame
import random
import time

pygame.init()



#main function
def main():
    #dictionary for pygame window information
    window_info = {
    "width": 720,
    "height": 720,
    "red": 100,
    "green": 100,
    "blue": 100
    }

    #dictionary for a start button
    start_button = {
        "width": 100,
        "height": 100,
        "red": 255,
        "green": 255,
    }
    #variable for the window
    window = pygame.display.set_mode((window_info["width"],window_info["height"]))

    #variable to tell if the user has quit/left
    running = True

    while running:
        #set color of window
        window.fill((window_info["red"], window_info["green"], window_info["blue"]))
        
        #ability to leave the memory game
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                running = False


        #update if it is still running
        if running:
            pygame.display.update()

main()