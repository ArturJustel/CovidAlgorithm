import sys
import struct

#The following function creates an adjacency matrix to represent a directed graph.
def MatrixMaker():
    file = open('sample-A.1.in', 'r')
    #file = sys.stdin

    cities, roads = map(int,file.readline().split())
    adArray = [[0 for i in range(cities)] for j in range(cities)]
    sourceNum , sinkNum = map(int,file.readline().split())
    sourceArray = list(map(int,file.readline().split()))
    sinkArray = list(map(int,file.readline().split()))

    for i in range(int(roads)):
        a,b,c = map(int,file.readline().split())
        adArray[a][b] = c

    file.close()
    return adArray,sourceNum,sinkNum,sourceArray,sinkArray

#The following function performs the breadth-first search algorithm on the adjacency matrix,
# to find the shortest path.
def BFS(adArray,queue,sinkArray,paths,visited):
    newQueue = []
    for node in queue:
        i=0
        for edge in adArray[node]:
            if edge>0:
                paths.append([node,i,edge])
                if i in sinkArray:
                    shortestPath = compPath(node,sourceArray,paths)
                    return shortestPath
                elif i in visited:
                    continue
                else:
                    visited.append(i)
                    newQueue.append(i)
            i+=1
    if newQueue.__len__()>0:
        BFS(adArray,newQueue,sinkArray,paths,visited)

#The following function compares the 
def compPath(node,sourceArray,paths):
    helpArray = list(reversed(paths))
    helpArray = helpArray[1:]
    for path in helpArray:
        if path[0] in sourceArray and path[1] == node:
            return paths
        if path[1] == node:
            compPath(path[0],sinkArray,paths)
        else:
            paths.remove(path)

#The following function performs the Ford-Fulkerson Algorithm on the shortest path to find the maximum flow.
# def FordFulkerson (shortestPath,sourceArray,sinkArray):
        

if __name__ == "__main__":
    adArray, sourceNum, sinNum, sourceArray, sinkArray = MatrixMaker()
    visited = sourceArray
    paths = []
    shortestPath = BFS(adArray,sourceArray,sinkArray,paths,visited)
    # max_flow = FordFulkerson(shortestPath,sourceArray,sinkArray)
    
