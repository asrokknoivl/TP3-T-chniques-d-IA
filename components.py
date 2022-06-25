import math
import random
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

    def solve_A_STAR(self):
        print(("CURRENTLY USING A*"))
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

    def solve_DFS(self):
        print("CURRENTLY USING DFS")
        paths= []
        paths.append({'path':[], 'agent_ids': agent_ids, 'agents':agents, 'void':empty_coord, 'steps':0})
        self.addToSeen(self.constructSet(agents))
        while True:
            current_path= paths.pop()
            if allAgentsArrived(current_path['agent_ids']):
                return current_path
            for agent in agentsThatCanMove(current_path['agents'], current_path['agent_ids'], current_path['void']):
                new_path= copy.deepcopy(current_path['path'])
                new_agent_ids= copy.deepcopy(current_path['agent_ids'])
                new_agents= copy.deepcopy(current_path['agents'])
                new_void= copy.deepcopy(current_path['void'])
                new_steps= current_path['steps']
                new_path.append(agent.id)
                new_agents[agent.y_current][agent.x_current]= -1
                new_agents[new_void[1]][new_void[0]]= "p"+str(agent.id)
                new_agent_ids["p"+str(agent.id)].x_current, new_agent_ids["p"+str(agent.id)].y_current, new_void[0], new_void[1]= new_void[0], new_void[1],new_agent_ids["p"+str(agent.id)].x_current, new_agent_ids["p"+str(agent.id)].y_current
                new_agent_ids["p"+str(agent.id)].recalcDist()                
                if self.constructSet(new_agents) in self.seen:
                    continue
                self.addToSeen(self.constructSet(new_agents))
                paths.append({'path':new_path, 'agent_ids': new_agent_ids, 'agents':new_agents, 'void':new_void, 'steps':new_steps})
    
    def solve_BFS(self):
        print("CURRENTLY USING BFS")
        paths= []
        paths.append({'path':[], 'agent_ids': agent_ids, 'agents':agents, 'void':empty_coord, 'steps':0})
        self.addToSeen(self.constructSet(agents))
        while True:
            current_path= paths[0]
            paths= paths[1:]
            if allAgentsArrived(current_path['agent_ids']):
                return current_path
            for agent in agentsThatCanMove(current_path['agents'], current_path['agent_ids'], current_path['void']):
                new_path= copy.deepcopy(current_path['path'])
                new_agent_ids= copy.deepcopy(current_path['agent_ids'])
                new_agents= copy.deepcopy(current_path['agents'])
                new_void= copy.deepcopy(current_path['void'])
                new_steps= current_path['steps']
                new_path.append(agent.id)
                new_agents[agent.y_current][agent.x_current]= -1
                new_agents[new_void[1]][new_void[0]]= "p"+str(agent.id)
                new_agent_ids["p"+str(agent.id)].x_current, new_agent_ids["p"+str(agent.id)].y_current, new_void[0], new_void[1]= new_void[0], new_void[1],new_agent_ids["p"+str(agent.id)].x_current, new_agent_ids["p"+str(agent.id)].y_current
                new_agent_ids["p"+str(agent.id)].recalcDist()                
                if self.constructSet(new_agents) in self.seen:
                    continue
                self.addToSeen(self.constructSet(new_agents))
                paths.append({'path':new_path, 'agent_ids': new_agent_ids, 'agents':new_agents, 'void':new_void, 'steps':new_steps})
                
    
    def solve_IDS(self, limit):
        print(f"CURRENTLY USING IDS WITH A MAX DEPTH OF {limit}")
        paths= []
        paths.append({'path':[], 'agent_ids': agent_ids, 'agents':agents, 'void':empty_coord, 'steps':0})
        self.addToSeen(self.constructSet(agents))
        while True:
            try:
                current_path= paths.pop()
            except:
                return []
            if allAgentsArrived(current_path['agent_ids']):
                return current_path
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
                if  new_steps>limit or self.constructSet(new_agents) in self.seen:
                    continue
                self.addToSeen(self.constructSet(new_agents))
                paths.append({'path':new_path, 'agent_ids': new_agent_ids, 'agents':new_agents, 'void':new_void, 'steps':new_steps})
  

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
        self.status= 'Active'
        self.remainingDistance= euclidianDistance(self.x_current, self.y_current, self.x_goal, self.y_goal)
        self.steps_taken= 0

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

    def move(self):
        self.x_current, self.y_current, empty_coord[0], empty_coord[1]= empty_coord[0], empty_coord[1],self.x_current, self.y_current
        agents[self.y_current][self.x_current]= "p"+str(self.id)
        agents[empty_coord[1]][empty_coord[0]]= -1
        self.recalcDist()

    def launch(self):
        while not self.hasReachedGoal():
            pass
        self.status= 'Arrived'
    
    def recalcDist(self):
        self.remainingDistance= euclidianDistance(self.x_current, self.y_current, self.x_goal, self.y_goal)
        
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
            print('..', end= ' ') if j== -1 else print(j, end= ' ')
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

def convMatrix(m):
    x = [[0]* size for _ in range(size)]
    i= 0
    j= 0
    while i< size:
        j=0
        while j< size:
            x[i][j]= int(''.join(list(m[i][j])[1:])) if str(m[i][j]).startswith("p") else 0
            j+=1
        i+=1
    return x

def getInvCount3(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, size*size):
        for j in range(i + 1, size*size):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
 
     
def isSolvable3(puzzle) :
    inv_count = getInvCount3([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)

N=4
def getInvCount(arr):
    arr1=[]
    for y in arr:
        for x in y:
            arr1.append(x)
    arr=arr1
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1,N * N):
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count+=1
         
     
    return inv_count
 
 
def findXPosition(puzzle):
    for i in range(N - 1,-1,-1):
        for j in range(N - 1,-1,-1):
            if (puzzle[i][j] == 0):
                return N - i
 
def isSolvable4(puzzle):
    invCount = getInvCount(puzzle)
    if (N & 1):
        return ~(invCount & 1)
 
    else:   
        pos = findXPosition(puzzle)
        if (pos & 1):
            return ~(invCount & 1)
        else:
            return invCount & 1

#print(convMatrix([['p9', 'p2', 'p3', 'p13'], ['p11', 'p14', 'p6', 'p8'], ['p5', 'p1', 'p10', 'p15'], ['p4', 'p12', -1, 'p7']]))
#print("yes") if isSolvable4(convMatrix([['p9', 'p2', 'p3', 'p13'], ['p11', 'p14', 'p6', 'p8'], ['p5', 'p1', 'p10', 'p15'], ['p4', 'p12', -1, 'p7']]))>0 else print("no")
