# Alec George, Jackson Hauley, and Tate Morgan, High Score Tracker

import pygame
import random
import time


def main():
    width = 720
    height = 720
    clicks = 0
    keep_running = True
    while keep_running:
        pygame.display.set_mode((width,height))
        pygame.display.set_caption("e")

        

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                color = 0
                r_offset = random.randint(0,255)
                g_offset = random.randint(0,255)
                b_offset = random.randint(0,255)
                for i in range(255):
                    width = random.randint(100,1000)
                    height = random.randint(100,1000)
                    screen = pygame.display.set_mode((width,height)).fill((abs((r_offset-color))%255,abs((g_offset-color))%255,abs((b_offset-color))%255))
                    pygame.display.update()
                    color += 1
                    time.sleep(0.001)
                clicks += 1

                if clicks == 5:
                    pygame.quit()
                    keep_running = False

        if keep_running:
            pygame.display.update()
    

    


main()
