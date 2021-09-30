#import module
import pygame
from pygame.locals import *


pygame.init()

run = True

while run:

    #event handless
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



pygame.quit()    