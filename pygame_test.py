import pygame
import random
from pygame.locals import *

pygame.init()


DISPLAY = pygame.display.set_mode((640, 400))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    x = random.randint(0,255)
    y = random.randint(0,255)
    t = random.randint(0,255)
    couleur = (x,y,t)
    DISPLAY.fill(couleur) 
    pygame.time.wait(150)
    pygame.display.flip()
    pygame.display.update()



