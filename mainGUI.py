from cgitb import grey
from json.encoder import ESCAPE
from turtle import window_height, window_width
import pygame
from pygame.locals import *
import sys
from components import *
import time
pygame.init()
FPS= 60

RED1= (0,0,255)
RED2= (0,0,235)
RED3= (0,0,215)
RED4= (0,0,195)
RED5= (0,0,175)
RED6= (0,0,155)
RED7= (0,0,145)
RED8= (0,0,125)
RED9= (0,0,105)
RED10= (0,0,165)
RED11= (0,0,155)
RED12= (0,0,145)
RED13= (0,0,135)
RED14= (0,0,125)
RED15= (0,0,115)
RED16= (0,0,105)
RED17= (0,0,95)
RED18= (0,0,85)
RED19= (0,0,75)
RED20= (0,0,65)
RED21= (0,0,55)
RED22= (0,0,45)
RED23= (0,0,35)
RED24= (0,0,25)
RED25= (0,0,15)

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
            color= colors[int((list(agents[y][x])[1]))] if agents[y][x]!= -1 else GREY
            pygame.draw.rect(window, color, (x* BLOCK_SIZE, y* BLOCK_SIZE, x* BLOCK_SIZE+ BLOCK_SIZE, y* BLOCK_SIZE+ BLOCK_SIZE))


def agentThread(id):
    agent = agent_ids["p"+str(id+1)]
    agent.launch()

def simulate():
    for i in range(agent_number):
        threading.Thread(target=agentThread, args=(i,)).start()


def gameLoop():
    mat= build()
    while(not isSolvable3(convMatrix(mat))):
        mat= build()
    master= Master()
    print("Preparing env...\n")
    try:
        solution= master.solve_DFS()
    except:
        print("NO SOLUTION WAS FOUND")
        return
    time.sleep(3)
    print("Initial state of the matrix:")
    displayGrid()
    path= solution['path']
    simulate()
    iteration= 0
    while True:
        if iteration< len(path):
            print(f"Iteration {iteration}")
            print(f"Agent {path[iteration]} to move")
            master.reorient(path[iteration])
            iteration+= 1 
        displayGrid()
        window.fill(GREY)
        eventHandler()
        drawBlocks()
        drawGrid()
        pygame.display.update()
        clock.tick(FPS)
        time.sleep(1)


gameLoop()
