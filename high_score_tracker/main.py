# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker


import pygame 
clock = pygame.time.Clock()
import sys 
import random
import time
  
pygame.init() # initializing the constructor 
 
# Names the window
pygame.display.set_caption('Random Title')

# Opens the window with the resolution
res = (720,720) 
screen = pygame.display.set_mode(res) 
  
# Colors
white = (255,255,255) 
color_light = (170,170,170)
color_dark = (100,100,100) 

alphabet = [chr(i) for i in range(97, 123)]

width = screen.get_width() 
height = screen.get_height() 
  
# Fonts
smallfont = pygame.font.SysFont('Arial',35) 
bigfont = pygame.font.SysFont('Arial',70) 

# COMPLETELY EDITABLE button location variables

quit_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" : 400 ,"y" : 360}, # Top left is 0,0
"text": "Quit",
"font": "Arial",
"fontsize": 35,
"hover_color": color_light,
"main_color": color_dark
}

reaction_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" :  180,"y" : 360}, # Top left is 0,0
"text": "Reaction", 
"font": "Arial",
"fontsize": 35,
"hover_color": color_light,
"main_color": color_dark
}

# END BUTTONS ==================================

def button(dict):
    if dict['StartPos']['x'] <= mouse[0] <= dict['StartPos']['x'] + dict['width'] and dict['StartPos']['y'] <= mouse[1] <= dict['StartPos']['y']+dict['height']: 
        pygame.draw.rect(screen,dict['hover_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is hovering
        pygame.display.set_caption('Button')
    else: 
        pygame.draw.rect(screen,dict['main_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is not touching
        pygame.display.set_caption('Click on a button!')
    screen.blit(pygame.font.SysFont(dict['font'],dict['fontsize']).render(dict['text'] , True , white),(dict['StartPos']['x']+0,dict['StartPos']['y'])) # Putting text on the button

running = True
while running: # Main Loop (break after quit)

    screen.fill((40,40,40)) # R G B (fills screen)

    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() # Stores mouse coordinates

    button(quit_button) # quit button creation
    button(reaction_button) # reaction button creation

    

    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            running = False
            break
              
        if ev.type == pygame.MOUSEBUTTONDOWN: # Mouse Click Checking
            # This is where you find out where the button was clicking then run something depending on the button

            if quit_button['StartPos']['x'] <= mouse[0] <= quit_button['StartPos']['x']+quit_button['width'] and quit_button['StartPos']['y'] <= mouse[1] <= quit_button['StartPos']['y']+quit_button['height']: 
                pygame.quit() 
                running = False
                break

            if reaction_button['StartPos']['x'] <= mouse[0] <= reaction_button['StartPos']['x']+reaction_button['width'] and reaction_button['StartPos']['y'] <= mouse[1] <= reaction_button['StartPos']['y']+reaction_button['height']: 
                reaction_running = True
                while reaction_running:

                    screen.fill((40,40,40))

                    screen.blit(bigfont.render('Reaction Game' , True , white),(100,60))
                    screen.blit(smallfont.render('Press the button once it turns green!' , True , white),(80,580))

                    pygame.draw.circle(screen, (255,0,0), (360,360) , 200)


                    for ev in pygame.event.get():

                        if ev.type == pygame.QUIT: 
                            reaction_running = False
                            running = False
                            pygame.quit() 
                            

                    if reaction_running == False:
                        break   

                    clock.tick(60) # Capping at 60fps so my PC doesnt die
                    pygame.display.update() # updates the frames of the game (always use)



    
    if running == False:
        break    

    clock.tick(60) # Capping at 60fps so my PC doesnt die
    pygame.display.update() # updates the frames of the game (always use)

        