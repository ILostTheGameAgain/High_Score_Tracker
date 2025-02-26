import pygame 
import random
from base_pygame import *
import sys

quit_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" : 400 ,"y" : 360}, # Top left is 0,0
"text": "Quit",
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100) ,
"text_offset": 0,
"text_color": (255,255,255)
}

menu_button = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" :  270,"y" : 630}, # Top left is 0,0
"text": "Menu", 
"font": "Arial",
"fontsize": 35,
"hover_color": (170,170,170),
"main_color": (100,100,100),
"text_offset": 0,
"text_color": (255,255,255)
}