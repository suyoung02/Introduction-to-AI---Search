import numpy as np
from queue import Queue
import math
def BFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
            
    path=[]
    visited = dict();
    visited={}
    
    q = []
    q.append(start)
    size = matrix.shape[0]
    i = 0
    visited[start] = start
    while len(q) > 0:
        while i < size:
            if(matrix[q[0],i] > 0):
                if(i not in visited.keys()):
                    q.append(i)
                    visited[i] = q[0]
                    if(i == end):
                        q.clear()
                        break
            i += 1
        if(len(q) > 0):
            q.pop(0)
        i = 0
    buffer = end
    while(buffer != start):
        path.append(buffer)
        buffer = visited[buffer]
    path.append(start)    
    path.reverse()
    return visited, path

def DFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited = dict();
    visited={}
    
    s = []
    s.append(start)
    size = matrix.shape[0]
    i = 0
    visited[start] = start
    while len(s) > 0:
        while i < size:
            if(matrix[s[-1],i] > 0):
                if(i not in visited.keys()):
                    s.append(i)
                    visited[i] = s[-2]
                    if(i == end):
                        s.clear()
                    break
            if(i == size - 1):
                s.pop()
            i += 1
        i = 0
        
    buffer = end
    while(buffer != start):
        path.append(buffer)
        buffer = visited[buffer]
    path.append(start)    
    path.reverse()
    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    path=[]
    visited = dict();
    visited={}
    size = matrix.shape[0]
    i = 0
    q = []
    q.append([0,start])
    visited[start] = start
    while len(q) > 0:
        while i < size:
            if(matrix[q[0][1],i] > 0 ):
                if(i not in visited.keys()):
                    q.append([matrix[q[0][1],i] + q[0][0],i])
                    visited[i] = q[0][1]
            i += 1
        i = 0
        q.sort()
        q.pop(0)
    
    buffer = end
    while(buffer != start):
        path.append(buffer)
        buffer = visited[buffer]
    path.append(start)    
    path.reverse()
    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited = dict();
    visited={}
    size = matrix.shape[0]
    i = 0
    q = []
    q.append([0,start,start])
    visited[start] = start
    while len(q) > 0:
        while i < size:
            if(matrix[q[0][1],i] > 0 ):
                    q.append([matrix[q[0][1],i],i,q[0][1]])
            i += 1
        i = 0
        q.pop(0)
        q.sort()
        if(q[0][1] not in visited.keys()):
            visited[q[0][1]] = q[0][2]
        if(q[0][1] == end):
            break
    
    buffer = end
    while(buffer != start):
        path.append(buffer)
        buffer = visited[buffer]
    path.append(start)    
    path.reverse()
    return visited, path
def euclidean(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited = dict();
    visited={}
    size = matrix.shape[0]
    i = 0
    q = []
    q.append([0,start,start])
    visited[start] = start
    heuristic = []
    while i < size:
        heuristic.append(euclidean(pos[i][0],pos[i][1],pos[end][0],pos[end][1]))
        i += 1
    i = 0
    while len(q) > 0:
        while i < size:
            if(matrix[q[0][1],i] > 0 ):
                    q.append([matrix[q[0][1],i] + heuristic[i],i,q[0][1]])
            i += 1
        i = 0
        q.pop(0)
        q.sort()
        print(q)
        if(q[0][1] not in visited.keys()):
            visited[q[0][1]] = q[0][2]
        if(q[0][1] == end):
            break
    
    buffer = end
    while(buffer != start):
        path.append(buffer)
        buffer = visited[buffer]
    path.append(start)    
    path.reverse()
    return visited, path

