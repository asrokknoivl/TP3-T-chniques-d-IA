from cgitb import grey
from json.encoder import ESCAPE
from turtle import window_height, window_width
import pygame
from pygame.locals import *
import sys
from main import *

pygame.init()
FPS= 60

RED1= (255, 0, 0)
RED2= (245, 0, 0)
RED3= (235, 0, 0)
RED4= (225, 0, 0)
RED5= (215, 0, 0)
RED6= (205, 0, 0)
RED7= (195, 0, 0)
RED8= (185, 0, 0)
RED9= (175, 0, 0)
RED10= (165, 0, 0)
RED11= (155, 0, 0)
RED12= (145, 0, 0)
RED13= (135, 0, 0)
RED14= (125, 0, 0)
RED15= (115, 0, 0)
RED16= (105, 0, 0)
RED17= (95, 0, 0)
RED18= (85, 0, 0)
RED19= (75, 0, 0)
RED20= (65, 0, 0)
RED21= (55, 0, 0)
RED22= (45, 0, 0)
RED23= (35, 0, 0)
RED24= (25, 0, 0)
RED25= (15, 0, 0)

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
colors[0]= RED1
colors[1]= RED2
colors[2]= RED3
colors[3]= RED4
colors[4]= RED5
colors[5]= RED6
colors[6]= RED7
colors[7]= RED8
colors[8]= RED9
colors[9]= RED10
colors[10]= RED11
colors[11]= RED12
colors[12]= RED13
colors[13]= RED14
colors[14]= RED15
colors[15]= RED16
colors[16]= RED17
colors[17]= RED18
colors[18]= RED19
colors[19]= RED20
colors[20]= RED21
colors[21]= RED22
colors[22]= RED23
colors[23]= RED24
colors[24]= RED25


WINDOW_WIDTH= 300
WINDOW_HEIGHT= 300
BLOCK_SIZE= 100

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
            color= colors[int((list(agents[y][x])[1]))] if agents[y][x]!= 0 else GREY
            pygame.draw.rect(window, color, (x* BLOCK_SIZE, y* BLOCK_SIZE, x* BLOCK_SIZE+ BLOCK_SIZE, y* BLOCK_SIZE+ BLOCK_SIZE))

def gameLoop():
    while True:
        window.fill(GREY)
        eventHandler()
        drawBlocks()
        drawGrid()
        pygame.display.update()
        clock.tick(FPS)


build()
simulate()
gameLoop()