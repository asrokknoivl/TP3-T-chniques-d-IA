import math
import random
import time
import copy
from turtle import st

size= 3
agent_number= size* size- 1
agents = [[0]* size for _ in range(size)]
step_size= 1
agent_list = []
agent_ids= {}
ALL_AGENTS_INACTIVE= False
empty_coord= [random.randint(0, size-1), random.randint(0, size-1)]
     

class Master:
    def __init__(self) -> None:
        self.seen= set()

    def reorient(self, id):
        agent_ids["p"+str(id)].move()

    def solve(self):
        paths= {}
        paths[f(0, agent_ids)]= [{'path':[], 'agent_ids': agent_ids, 'agents':agents, 'void':empty_coord, 'steps':0}]

        while True:
            current_path_n= min(paths)
            try:
                current_path= paths[current_path_n][0]
            except:
                del(paths[current_path_n])
                continue
            if allAgentsArrived(current_path['agent_ids']):
                return current_path
            del(paths[current_path_n][0])
            for agent in agentsThatCanMove(current_path['agents'], current_path['agent_ids'], current_path['void']):
                new_path= copy.deepcopy(current_path['path'])
                new_agent_ids= copy.deepcopy(current_path['agent_ids'])
                new_agents= copy.deepcopy(current_path['agents'])
                new_void= copy.deepcopy(current_path['void'])
                new_steps= current_path['steps']+1
                new_path.append(agent.id)
                new_agents[agent.y_current][agent.x_current]= -1
                new_agents[new_void[1]][new_void[0]]= "p"+str(agent.id)
                new_agent_ids["p"+str(agent.id)].x_current, new_agent_ids["p"+str(agent.id)].y_current, new_void[0], new_void[1]= new_void[0], new_void[1],new_agent_ids["p"+str(agent.id)].x_current, new_agent_ids["p"+str(agent.id)].y_current
                new_agent_ids["p"+str(agent.id)].recalcDist()                
                if self.constructSet(new_agents) in self.seen:
                    continue
                self.addToSeen(self.constructSet(new_agents))
                try:
                    paths[f(new_steps, new_agent_ids)].append({'path':new_path, 'agent_ids': new_agent_ids, 'agents':new_agents, 'void':new_void, 'steps':new_steps})
                except:
                    paths[f(new_steps, new_agent_ids)]=[{'path':new_path, 'agent_ids': new_agent_ids, 'agents':new_agents, 'void':new_void, 'steps':new_steps}]
                
    
                
    def constructSet(self, agents):
        s= ""
        for i in agents:
            for j in i:
                s+= str(j)
        return hash(s)

    def addToSeen(self, s):
        self.seen.add(s)

def h(agent_ids):
    h= 0
    for agent in agent_ids:
        h+= agent_ids[agent].remainingDistance
    return h
    
def f(steps, agent_ids):
    return h(agent_ids)+ steps


class Agent:
    def __init__(self, id, x_current, y_current, x_goal, y_goal) -> None:
        self.x_prev= -9999
        self.y_prev= -9999
        self.x_current= x_current
        self.y_current= y_current
        self.x_goal= x_goal
        self.y_goal= y_goal
        self.id= id
        self.conflictCheck= 0
        self.ok= False
        self.status= 'Active'
        self.remainingDistance= euclidianDistance(self.x_current, self.y_current, self.x_goal, self.y_goal)
        self.previousCaseHolder= 0
        self.steps_taken= 0
        self.green_light= None

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
        while axe== 'x':
            if self.isAvailable(self.x_current+ 1, self.y_current):
                agents[self.y_current][self.x_current]= 0
                self.x_current+= 1
                agents[self.y_current][self.x_current]= "p"+str(self.id)
                break
            elif self.isAvailable(self.x_current- 1, self.y_current):
                agents[self.y_current][self.x_current]= 0
                self.x_current-= 1
                agents[self.y_current][self.x_current]= "p"+str(self.id)
                break
            else: 
                if self.y_current> self.y_prev:
                    agents[self.y_current][self.x_current]= 0
                    self.y_current-= 1
                    self.y_prev-= 1
                    agents[self.y_current][self.x_current]= "p"+str(self.id)

                else:
                    agents[self.y_current][self.x_current]= 0
                    self.y_current+= 1
                    self.y_prev+= 1
                    agents[self.y_current][self.x_current]= "p"+str(self.id)

        while axe== 'y':
            if self.isAvailable(self.x_current, self.y_current+ 1):
                agents[self.y_current][self.x_current]= 0
                self.y_current+= 1
                agents[self.y_current][self.x_current]= "p"+str(self.id)
                break
            elif self.isAvailable(self.x_current, self.y_current- 1):
                agents[self.y_current][self.x_current]= 0
                self.y_current-= 1
                agents[self.y_current][self.x_current]= "p"+str(self.id)
                break
            else: 
                if self.x_current> self.x_prev:
                    agents[self.y_current][self.x_current]= 0
                    self.x_current-= 1
                    self.x_prev-= 1
                    agents[self.y_current][self.x_current]= "p"+str(self.id)

                else:
                    agents[self.y_current][self.x_current]= 0
                    self.x_current+= 1
                    self.x_prev+= 1
                    agents[self.y_current][self.x_current]= "p"+str(self.id)

        time.sleep(1)
        
    def findNextMove_GreedySearch(self):
        distances= euclidianDistances(self, self.x_current, self.y_current, self.x_goal, self.y_goal)
        self.remainingDistance= min(distances)
        return distances[min(distances)]

    def findNextMove_ASTAR(self):   
        distances= euclidianDistances(self, self.x_current, self.y_current, self.x_goal, self.y_goal, True)
        self.remainingDistance= min(distances)
        return distances[min(distances)]


    def isAvailable(self, x, y):
        return agents[y][x]== 0 or str(agents[y][x]).startswith('X')
    
    def move(self):
        self.x_current, self.y_current, empty_coord[0], empty_coord[1]= empty_coord[0], empty_coord[1],self.x_current, self.y_current
        agents[self.y_current][self.x_current]= "p"+str(self.id)
        agents[empty_coord[1]][empty_coord[0]]= -1
        self.recalcDist()
        


    def launch(self):
        while not self.hasReachedGoal():
            pass
        self.status= 'Arrived'
    
    def move__(self):
        while not self.hasReachedGoal():
            #print([i.id for i in agentsThatCanMove()])
            if agentRepositionRequest(self.id):
                agentsToAsk= agentsThatCanMove()
                i= 0
                while i< len(agentsToAsk):
                    agent= agentsToAsk[i]
                    if self.id== agent.id or agent.status== 'Arrived' or agent.moveRequest(self):
                        i+= 1
                    #print("need approval", self.id, i)
                    #print(self.id, '  ', i, [i.id for i in agentsToAsk], agent.id, agent.moveRequest(self), ' ', self.id ==agent.id)
                self.x_current, self.y_current, empty_coord[0], empty_coord[1]= empty_coord[0], empty_coord[1], self.x_current, self.y_current
                self.steps_taken+= 1
                self.remainingDistance= euclidianDistance(self.x_current, self.y_current, self.x_goal, self.y_goal)
                self.updatePos()
            time.sleep(3*self.id + 5)


    def updatePos(self):        
        agents[self.y_current][self.x_current]= "p"+str(self.id)if self.id!= 8 else -1
        agents[empty_coord[1]][empty_coord[0]]= -1

    def moveRequest(self, agent):
        rd1= euclidianDistance(empty_coord[0], empty_coord[1], self.x_goal, self.y_goal)
        rd2= euclidianDistance(empty_coord[0], empty_coord[1], agent.x_goal, agent.y_goal)
        if rd1== rd2:
            return self.id> agent.id
        return rd1> rd2

    def move_(self, x, y):
        counter= 0
        while not self.isAvailable(x, y):
            self.status= 'Waiting, potential conflict'
            time.sleep(1)
            if counter >= 3:
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
        agents[self.y_current][self.x_current]= "p"+str(self.id) if self.id!= 8 else -1
        self.steps_taken+= 1
        self.remainingDistance= euclidianDistance(self.x_current, self.y_current, self.x_goal, self.y_goal)
        time.sleep(2)

    def recalcDist(self):
        self.remainingDistance= euclidianDistance(self.x_current, self.y_current, self.x_goal, self.y_goal)
        

    def fightOrFlight(self, x, y):
        agent= agent_list[int(list(str(agents[y][x]))[1])]
        print(agent.id)
        agent_next_move= agent.findNextMove_GreedySearch()
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
        axe= self.changeDirection('y') if self.x_current== agent.x_current else self.changeDirection('x')

    def hasReachedGoal(self):
        return self.remainingDistance==0


def euclidianDistance(x, y, x_goal, y_goal): #heuristic function - distance
    x_diff = abs(x - x_goal)
    y_diff = abs(y - y_goal)
    euclidianDistance = math.sqrt(x_diff * x_diff + y_diff * y_diff)
    return euclidianDistance

def euclidianDistances(agent, x, y ,x_goal ,y_goal, A_STAR= False): #GREEDY BEST FIRST SEARCH
    x_right= x + step_size
    x_left= x - step_size
    y_down= y + step_size
    y_up= y - step_size
    distances= {}
    d1= euclidianDistance(x_right, y, x_goal, y_goal)+ agent.steps_taken if A_STAR== True else euclidianDistance(x_right, y, x_goal, y_goal)
    d2= euclidianDistance(x_left, y, x_goal, y_goal)+ agent.steps_taken if A_STAR== True else euclidianDistance(x_left, y, x_goal, y_goal)
    d3= euclidianDistance(x, y_down, x_goal, y_goal)+ agent.steps_taken if A_STAR== True else euclidianDistance(x, y_down, x_goal, y_goal)
    d4= euclidianDistance(x, y_up, x_goal, y_goal)+ agent.steps_taken if A_STAR== True else euclidianDistance(x, y_up, x_goal, y_goal)
    distances[d1]= (x_right, y) 
    distances[d2]= (x_left, y) 
    distances[d3]= (x, y_down) 
    distances[d4]= (x, y_up) 
    return distances

def displayGrid():
    print()
    for i in agents:
        for j in i:
            print('..', end= ' ') if j== 0 else print(j, end= ' ')
        print()
    print()


def build():
    reserved_coordinates= []
    reserved_coordinates.append((empty_coord[0],empty_coord[1]))
    agents[empty_coord[1]][empty_coord[0]]= -1
    id= 1
    for i in range(size):
        for j in range(size):
            if i== size-1 and j== size-1:
                continue
            x= random.randint(0, size-1)
            y= random.randint(0, size-1)
            while (x,y) in reserved_coordinates:
                x= random.randint(0, size-1)
                y= random.randint(0, size-1)
            reserved_coordinates.append((x,y))
            a= Agent(id, x, y, j, i)
            agent_list.append(a)
            agents[y][x]= "p"+str(id)
            agent_ids["p"+str(id)]= a
            id += 1
    return agents

def allAgentsArrived(agent_ids):
    for agent in agent_ids:
        if not agent_ids[agent].hasReachedGoal():
            return False
    return True

def agentsThatCanMove(agents, agent_ids, empty_coord):
    l= []
    l+= [agents[empty_coord[1]+1][empty_coord[0]]] if empty_coord[1]+1 in range(size) else []
    l+= [agents[empty_coord[1]-1][empty_coord[0]]] if empty_coord[1]-1 in range(size) else []
    l+= [agents[empty_coord[1]][empty_coord[0]+1]] if empty_coord[0]+1 in range(size) else []
    l+= [agents[empty_coord[1]][empty_coord[0]-1]] if empty_coord[0]-1 in range(size) else []
    return [agent_ids[x] for x in l if str(x).startswith("p")]

def agentRepositionRequest(id):
    l= [i.id for i in agentsThatCanMove()]
    return id in l



def nextAgentToMove(self):
    h_val= 66666666
    agent_id= 66666666
    for agent in agentsThatCanMove():
        agent.x_current, agent.y_current, empty_coord[0], empty_coord[1]= empty_coord[0], empty_coord[1], agent.x_current, agent.y_current
        h= self.heuristic()
        self.updatePos()
        s= constructSet()
        if s not in seen and h< h_val:
            h_val= h
            agent_id= agent.id
            addToSeen(s)
            agent.x_current, agent.y_current, empty_coord[0], empty_coord[1]= empty_coord[0], empty_coord[1], agent.x_current, agent.y_current
            self.updatePos()
    return agent_id


def convMatrix(m):
    x = [[0]* 3 for _ in range(3)]
    i= 0
    j= 0
    while i< 3:
        j=0
        while j< 3:
            x[i][j]= int(''.join(list(m[i][j])[-1])) if str(m[i][j]).startswith("p") else m[i][j] 
            j+=1
        i+=1
    return x

def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
 
     
def isSolvable(puzzle) :
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)
