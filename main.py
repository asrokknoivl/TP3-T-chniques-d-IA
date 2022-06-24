import random
import logging
import threading
from components import *

def agentThread(id):
    agent = agent_list[id]
    agent.launch()   

def display():
    iteration= 0
    while True:
        displayGrid()            
        print(f"Iteration {iteration}")
        for agent in agent_list:
            print(f"Agent {agent.id}, status: {agent.status}, current position ({agent.x_current}, {agent.y_current}), goal position ({agent.x_goal}, {agent.y_goal})")
        iteration+= 1
        if allAgentsArrived(agent_ids):
            break
        time.sleep(1)
    time.sleep(1)
    displayGrid()
    for agent in agent_list:
        print(f"Iteration {iteration}")
        print(f"Agent {agent.id}, status: {agent.status}, previous position ({agent.x_prev}, {agent.y_prev}), current position ({agent.x_current}, {agent.y_current}), goal position ({agent.x_goal}, {agent.y_goal})")
    print()
    print('ALL AGENTS HAVE ARRIVED TO THEIR GOAL POSITIONS!')

def simulate():
    for i in range(agent_number):
        threading.Thread(target=agentThread, args=(i,)).start()

if __name__ == '__main__':
    mat= build()
    while(not isSolvable(convMatrix(mat))):
        mat= build()
    master= Master()
    solution= master.solve()
    print("Preparing env...\n")
    time.sleep(3)
    print("Initial state of the matrix:")
    displayGrid()
    path= solution['path']
    simulate()
    for iteration, agent in enumerate(path):
        print(f"Iteration {iteration}")
        print(f"Agent {agent} to move")
        master.reorient(agent)
        displayGrid()
    for agent in agent_list:
        print(f"Agent {agent.id}: ", agent.status, agent.remainingDistance)

