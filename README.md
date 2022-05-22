# TP3-Téchniques-d'IA
AI school project, Multi-Agent interaction

The idea is to simulate a grid where several agents are placed on a certain position with the intention of moving to another one, all moving at the same time.
Agents can't exist on the same case at the same time.
Each agent has full knowledge of the environment/grid.
Agents can communicate through messages.

Simple strategies that agents can follow:
- BFS
- DFS
- IDFS
- Greedy search
- A*

Function to find the next move
in conflict, priority goes to the agent with weaker weight/smaller distance to goal, if distances are equal agent to go is chosen based on id.
