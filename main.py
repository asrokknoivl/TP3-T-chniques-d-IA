import random
import logging
import threading
from components import *

agent_list = []
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
    agent_list.append(Agent(id, x, y, x_g, y_g))

def agentThread(id):
    print(f"Thread {id}: starting")
    agent = agent_list[id]
    print(agent.getYOrigin())
    print(agent.getXOrigin())
    print(agent.getYGoal())
    print(agent.getXGoal())
    agents[agent.getYOrigin()][agent.getXOrigin()]= "p"+str(agent.getId())
    agents[agent.getYGoal()][agent.getXGoal()]= "X"+str(agent.getId())
    while not agent.hasReachedGoal():
        x,y= agent.findNextMove()
        print(f"""Agent {id} is currently at the coordinates: ({agent.getXOrigin()}, {agent.getYOrigin()})
Agent {id} has moved to the coordinates: ({x}, {y})
Agent {id} goal position: ({agent.getXGoal()}, {agent.getYGoal()})""")
        agent.move(x,y)
        #displayGrid()
        time.sleep(1)
    agents[agent.getYGoal()][agent.getXGoal()]= 0
    print(f"Thread {id}: finishing")


def main():
    for i in range(agent_number):
        threading.Thread(target=agentThread, args=(i,)).start()


if __name__ == '__main__':
    main()