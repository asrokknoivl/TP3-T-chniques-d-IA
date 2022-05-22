import math
import time

grid_w= 25
grid_h= 25
agents = [[0]* grid_w for _ in range(grid_h)]
step_size= 1

class Agent:
    def __init__(self, id, x_origin, y_origin, x_goal, y_goal) -> None:
        self.x_origin= x_origin
        self.y_origin= y_origin
        self.y_goal= y_goal
        self.x_goal= x_goal
        self.id= id

    def setId(self, id):
        self.id= id

    def getId(self):
        return self.id

    def setXOrigin(self, n):
        self.x_origin= n
    
    def setYOrigin(self, n):
        self.y_origin= n
        
    def setXGoal(self, n):
        self.x_goal= n
        
    def setYGoal(self, n):
        self.x_goal= n

    def getXOrigin(self):
        return self.x_origin
        
    def getYOrigin(self):
        return self.y_origin
        
    def getXGoal(self):
        return self.x_goal
        
    def getYGoal(self):
        return self.y_goal

    def moveUp(self):
        self.x_origin -= 5

    def moveDown(self):
        self.x_origin += 5
    
    def moveRight(self):
        self.y_origin += 5
        
    def moveLeft(self):
        self.y_origin -= 5
        
    def findNextMove(self):
        distances= euclidianDistances(self.x_origin, self.y_origin, self.x_goal, self.y_goal)
        return distances[min(distances)]

    def isAvailable(self, x, y):
        return agents[y][x]== 0 if (x,y)!= (self.x_goal, self.y_goal) else True
    
    def move(self, x, y):
        while not self.isAvailable(x, y):
            pass
        agents[self.y_origin][self.x_origin]= 0
        agents[y][x]= "p"+str(self.id)
        self.x_origin= x
        self.y_origin= y

    def hasReachedGoal(self):
        return (self.getXOrigin(), self.getYGoal())== (self.getXGoal(), self.getYGoal())




def euclidianDistance(x, y, x_goal, y_goal): #heuristic function
    x_diff = abs(x - x_goal)
    y_diff = abs(y - y_goal)
    euclidianDistance = math.sqrt(x_diff * x_diff + y_diff * y_diff)
    return euclidianDistance

def euclidianDistances(x, y ,x_goal ,y_goal): #GREEDY BEST FIRST SEARCH
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

displayGrid()
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