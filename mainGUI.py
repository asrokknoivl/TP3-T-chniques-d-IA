from cgitb import grey
from json.encoder import ESCAPE
from turtle import window_height, window_width
import pygame
from pygame.locals import *
import sys
from main import *

pygame.init()
FPS= 60

GREEN= (0, 204, 0)
RED= (255, 51, 51)
BLUE= (51, 51, 255)
ORANGE= (255, 128, 0)
PINK= (255, 0, 127)
DARK_VIOLET= (204, 0, 204)
YELLOW= (255, 255, 51)
INDIGO= (76, 0, 153)
LIGHT_BLUE= (153, 255, 255)
LIGHT_PINK= (255, 153, 204)
GREY= (160, 160, 160)

colors= {}
colors[0]= GREEN
colors[1]= RED
colors[2]= BLUE
colors[3]= ORANGE
colors[4]= PINK
colors[5]= DARK_VIOLET
colors[6]= YELLOW
colors[7]= INDIGO
colors[8]= LIGHT_BLUE
colors[9]= LIGHT_PINK

WINDOW_WIDTH= 625
WINDOW_HEIGHT= 625
BLOCK_SIZE= 25

window= pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("AGENT SIMULATION")

clock= pygame.time.Clock()

def drawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        pygame.draw.line(window, (0, 0, 0), (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(window, (0, 0, 0), (0, y), (WINDOW_WIDTH, y))

def eventHandler():
    for event in pygame.event.get():
        if event.type== QUIT:
            sys.exit()
        elif event.type== KEYDOWN and event.key== K_ESCAPE:
            sys.exit()

def drawBlocks():
    for x,_ in enumerate(agents):
        for y, __ in enumerate(_):
            color= colors[int((list(agents[x][y])[1]))] if agents[x][y]!= 0 else GREY
            pygame.draw.rect(window, color, (x* BLOCK_SIZE, y* BLOCK_SIZE, x* BLOCK_SIZE+ BLOCK_SIZE, y* BLOCK_SIZE+ BLOCK_SIZE))

def gameLoop():
    while True:
        window.fill(GREY)
        eventHandler()
        drawBlocks()
        drawGrid()
        pygame.display.update()
        clock.tick(FPS)

simulate()
gameLoop()