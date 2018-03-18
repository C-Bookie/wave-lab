
import pygame, sys
from pygame.locals import *

import numpy as np

width = 800
height = 300

def init():
    pygame.init()

    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption('Drawing')


def draw(sample, f):
    global DISPLAYSURF
    DISPLAYSURF.fill((32, 32, 32))

    scale = (f/width)*4
#    scale = 1
    last = (0,height/2);

    x = 0
    while x < width:
        cur = (x, height-(sample.item(int(np.floor(x*scale)))*height/2 + height/2))
        pygame.draw.line(DISPLAYSURF, (224, 224, 224), last, cur)
        last = cur
        x+=1

    paint()


def paint():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

