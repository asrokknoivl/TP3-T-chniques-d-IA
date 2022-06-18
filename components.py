import math
import random
import time

agent_number= 10
grid_w= 25
grid_h= 25
agents = [[0]* grid_w for _ in range(grid_h)]
step_size= 1
agent_list = []


class Agent:
    def __init__(self, id, x_current, y_current, x_goal, y_goal) -> None:
        self.x_prev= -9999
        self.y_prev= -9999
        self.x_current= x_current
        self.y_current= y_current
        self.y_goal= y_goal
        self.x_goal= x_goal
        self.id= id
        self.conflictCheck= 0
        self.ok= False
        self.status= 'Active'
        self.remainingDistance= euclidianDistance(self.x_current, self.y_current, self.x_goal, self.y_goal)
        self.previousCaseHolder= 0

    def setId(self, id):
        self.id= id

    def getId(self):
        return self.id

    def setXOrigin(self, n):
        self.x_current= n
    
    def setYOrigin(self, n):
        self.y_current= n
        
    def setXGoal(self, n):
        self.x_goal= n
        
    def setYGoal(self, n):
        self.x_goal= n

    def getXOrigin(self):
        return self.x_current
        
    def getYOrigin(self):
        return self.y_current
        
    def getXGoal(self):
        return self.x_goal
        
    def getYGoal(self):
        return self.y_goal

    def moveUp(self):
        self.x_current -= 5

    def moveDown(self):
        self.x_current += 5
    
    def moveRight(self):
        self.y_current += 5
        
    def moveLeft(self):
        self.y_current -= 5

    def changeDirection(self, axe):    
        agents[self.y_current][self.x_current]= 0
        if axe== 'x':
            d= random.choice([1, -1])
            self.y_current += 1* d
            while not self.isAvailable(self.x_current, self.y_current):
                self.x_current+= 1* d
                d= random.choice([1, -1])
                agents[self.y_current][self.x_current]= "p"+str(self.id)
            agents[self.y_current][self.x_current]= "p"+str(self.id)
        elif axe== 'y':
            d= random.choice([1, -1])
            self.x_current += 1* d
            while not self.isAvailable(self.x_current, self.y_current):
                self.y_current+= 1* d
                d= random.choice([1, -1])
                agents[self.y_current][self.x_current]= "p"+str(self.id)
            agents[self.y_current][self.x_current]= "p"+str(self.id)
        time.sleep(1)
        return None
        
    def findNextMove(self):
        distances= euclidianDistances(self.x_current, self.y_current, self.x_goal, self.y_goal, self)
        self.remainingDistance= min(distances)
        return distances[min(distances)]

    def isAvailable(self, x, y):
        return agents[y][x]== 0 or str(agents[y][x]).startswith('X')
    
    def move(self, x, y):
        counter= 0
        while not self.isAvailable(x, y):
            self.status= 'Waiting, potential conflict'
            time.sleep(1)
            if counter >= 5:
                self.status= 'At conflict, currently being resolved'
                self.fightOrFlight(x, y)
                return
            counter+= 1
        self.status= 'Active'
        self.x_prev= self.x_current
        self.y_prev= self.y_current
        self.x_current= x
        self.y_current= y
        agents[self.y_prev][self.x_prev]= self.previousCaseHolder
        self.previousCaseHolder= agents[self.y_current][self.x_current]
        agents[self.y_current][self.x_current]= "p"+str(self.id)

        

    def fightOrFlight(self, x, y):
        agent= agent_list[int(list(str(agents[y][x]))[1])]
        print(agent.id)
        agent_next_move= agent.findNextMove()
        agent_next_x= agent_next_move[0]
        agent_next_y= agent_next_move[1]
        if self.x_current== agent_next_x and self.y_current== agent_next_y:
            if self.remainingDistance > agent.remainingDistance:
                pass
            else:
                self.requestToOpenRoad(agent)

    def requestToOpenRoad(self, agent):
        agent.recieveToOpenRoad(self)

    def recieveToOpenRoad(self, agent):
        if agent.remainingDistance <= self.remainingDistance:
            axe= self.changeDirection('y') if self.x_current== agent.x_current else self.changeDirection('x')

    def hasReachedGoal(self):
        return (self.x_current, self.y_current)== (self.x_goal, self.y_goal)




def euclidianDistance(x, y, x_goal, y_goal): #heuristic function - distance
    x_diff = abs(x - x_goal)
    y_diff = abs(y - y_goal)
    euclidianDistance = math.sqrt(x_diff * x_diff + y_diff * y_diff)
    return euclidianDistance

def euclidianDistances(x, y ,x_goal ,y_goal, agent): #GREEDY BEST FIRST SEARCH
    x_right= x + step_size
    x_left= x - step_size
    y_down= y + step_size
    y_up= y - step_size
    distances= {}
    distances[euclidianDistance(x_right, y, x_goal, y_goal)]= (x_right, y) 
    distances[euclidianDistance(x_left, y, x_goal, y_goal)]= (x_left, y) 
    distances[euclidianDistance(x, y_down, x_goal, y_goal)]= (x, y_down) 
    distances[euclidianDistance(x, y_up, x_goal, y_goal)]= (x, y_up) 
    return distances

def displayGrid():
    print()
    for i in agents:
        for j in i:
            print('--', end= ' ') if j== 0 else print(j, end= ' ')
        print()
    print()
    


if __name__== '__main__':
    agent1= Agent(1, 4, 6, 12, 15)
    agents[agent1.getYOrigin()][agent1.getXOrigin()]= "p"+str(agent1.getId())
    agents[agent1.getYGoal()][agent1.getXGoal()]= "X"+str(agent1.getId())
    while not agent1.hasReachedGoal():
        x,y= agent1.findNextMove()
        print(f"Next best case: {x}, {y}" )
        agent1.move(x,y)
        displayGrid()
        time.sleep(1)
        
    print('Agent 1 has arrived to its goal position')