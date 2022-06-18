import random
import logging
import threading
from components import *

ALL_AGENTS_INACTIVE= False
reserved_coordinates= []

for id in range(agent_number):
    x= random.randint(0, grid_w-1)
    y= random.randint(0, grid_h-1)
    x_g= random.randint(0, grid_w-1)
    y_g= random.randint(0, grid_h-1)
    while (x,y) in reserved_coordinates:
        x= random.randint(0, grid_w-1)
        y= random.randint(0, grid_h-1)
    while (x_g, y_g) in reserved_coordinates:
        x_g= random.randint(0, grid_w-1)
        y_g= random.randint(0, grid_h-1)
    reserved_coordinates.append((x,y))
    reserved_coordinates.append((x_g,y_g))
    agent_list.append(Agent(id, x, y, x_g, y_g))
    agents[y][x]= "p"+str(id)
    agents[y_g][x_g]= "X"+str(id)


def allAgentsArrived():
    for agent in agent_list:
        if not agent.hasReachedGoal():
            return False
    return True

def agentThread(id):
    agent = agent_list[id]
    agents[agent.getYOrigin()][agent.getXOrigin()]= "p"+str(agent.getId())
    agents[agent.getYGoal()][agent.getXGoal()]= "X"+str(agent.getId())
    while not agent.hasReachedGoal():
        x,y= agent.findNextMove()
        #print(f"""Agent {id} is currently at the coordinates: ({agent.getXOrigin()}, {agent.getYOrigin()})
#Agent {id} has moved to the coordinates: ({x}, {y})
#Agent {id} goal position: ({agent.getXGoal()}, {agent.getYGoal()})""")
        agent.move(x,y)
        time.sleep(1)
    agents[agent.getYGoal()][agent.getXGoal()]= 0
    agent.status= 'Arrived'
    #print(f"Thread {id}: finishing")


def display():
    iteration= 0
    while True:
        displayGrid()
        for agent in agent_list:
            print(f"Iteration {iteration}")
            print(f"Agent {agent.id}, status: {agent.status}, previous position ({agent.x_prev}, {agent.y_prev}), current position ({agent.x_current}, {agent.y_current}), goal position ({agent.x_goal}, {agent.y_goal})")
        time.sleep(1)
        iteration+= 1
        if allAgentsArrived():
            break
    time.sleep(1)
    displayGrid()
    for agent in agent_list:
        print(f"Iteration {iteration}")
        print(f"Agent {agent.id}, status: {agent.status}, previous position ({agent.x_prev}, {agent.y_prev}), current position ({agent.x_current}, {agent.y_current}), goal position ({agent.x_goal}, {agent.y_goal})")
    print()
    print('ALL AGENTS HAVE ARRIVED TO THEIR GOAL POSITIONS!')

def simulate():
    threading.Thread(target= display).start()
    for i in range(agent_number):
        threading.Thread(target=agentThread, args=(i,)).start()


if __name__ == '__main__':
    simulate()