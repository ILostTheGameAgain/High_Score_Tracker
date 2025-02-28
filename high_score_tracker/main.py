# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker
import pygame
clock = pygame.time.Clock()
from file_functions import *
from reaction_time_game import *
from math_quiz import *
from base_pygame import *
from memory_game import *
start_highscores(highscores,data)

pygame.init()

quit_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" : 550 ,"y" : 650}, # Top left is 0,0
"text": "Quit",
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100) ,
"text_offset": 35,
"text_color": (255,255,255)
}
reaction_button = {
"width" : 150, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" : 350 ,"y" : 650}, # Top left is 0,0
"text": "Reaction",
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100) ,
"text_offset": 5,
"text_color": (255,255,255)
}
quiz_button = {
"width" : 150, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" : 150 ,"y" : 650}, # Top left is 0,0
"text": "Quiz",
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100) ,
"text_offset": 35,
"text_color": (255,255,255)
}
memory_button = {
"width" : 150, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" : 50 ,"y" : 650}, # Top left is 0,0
"text": "Quiz",
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100) ,
"text_offset": 35,
"text_color": (255,255,255)
}

pygame.display.set_mode((720,720))

def main():
    run = True
    while run:
        pygame.display.set_caption('High Score Tracker')

        mouse = pygame.mouse.get_pos()

        screen.fill((40,40,40))
        screen.blit(bigfont.render('High Score Tracker' , True , white),(100,60))
        button(quit_button)
        button(reaction_button)
        button(quiz_button)
        button(memory_button)


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                run = False

            if ev.type == pygame.MOUSEBUTTONDOWN: # Mouse Click Checking

                if quit_button['StartPos']['x'] <= mouse[0] <= quit_button['StartPos']['x']+quit_button['width'] and quit_button['StartPos']['y'] <= mouse[1] <= quit_button['StartPos']['y']+quit_button['height']: # Checking in this range for clicking the button
                    pygame.quit() 
                    running = False
                    run = False
                    break
                if reaction_button['StartPos']['x'] <= mouse[0] <= reaction_button['StartPos']['x']+reaction_button['width'] and reaction_button['StartPos']['y'] <= mouse[1] <= reaction_button['StartPos']['y']+reaction_button['height']: # Checking in this range for clicking the button
                    reaction_game() 
                    run = True
                    break
                if quiz_button['StartPos']['x'] <= mouse[0] <= quiz_button['StartPos']['x']+quiz_button['width'] and quiz_button['StartPos']['y'] <= mouse[1] <= quiz_button['StartPos']['y']+quiz_button['height']: # Checking in this range for clicking the button
                    math_quiz() 
                    run = True
                    break
                if memory_button['StartPos']['x'] <= mouse[0] <= memory_button['StartPos']['x']+memory_button['width'] and memory_button['StartPos']['y'] <= mouse[1] <= memory_button['StartPos']['y']+memory_button['height']: # Checking in this range for clicking the button
                    memory() 
                    run = True
                    break
        if run:
            pygame.display.update()
        clock.tick(fps)
main()

