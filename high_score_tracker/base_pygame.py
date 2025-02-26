# Jackson, Alec, Tate, Base pygame functions
import pygame
res = (720,720)
screen = pygame.display.set_mode(res)

"""
example_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" :  270,"y" : 630}, # Top left is 0,0
"text": "Menu", 
"font": "Arial",
"fontsize": 35,
"hover_color": (80,80,80),
"main_color": (40,40,40),
"text_offset": 0,
"text_color": (255,255,255)
}
"""

# button(example_button)

def button(dict):
    mouse = pygame.mouse.get_pos() # Stores mouse coordinates
    if dict['StartPos']['x'] <= mouse[0] <= dict['StartPos']['x'] + dict['width'] and dict['StartPos']['y'] <= mouse[1] <= dict['StartPos']['y']+dict['height']: 
        pygame.draw.rect(screen,dict['hover_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is hovering
    else: 
        pygame.draw.rect(screen,dict['main_color'],[dict['StartPos']['x'],dict['StartPos']['y'],dict['width'],dict['height']]) # If mouse is not touching
    screen.blit(pygame.font.SysFont(dict['font'],dict['fontsize']).render(dict['text'] , True , dict["text_color"]),(dict['StartPos']['x']+dict["text_offset"],dict['StartPos']['y'])) # Putting text on the button