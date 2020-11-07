import sys
import struct

#this function reads the test file and assigns it the variables and makes the adjencecy matrix for the algoirithm to follow

def MatrixMaker():

    file = open('samples-A/1.in', 'r')
    #file = sys.stdin

    cities, roads = map(int,file.readline().split())

    adArray = [[0 for i in range(cities)] for j in range(cities)]

    sourceNum , sinkNum = map(int,file.readline().split())

    sourceArray = map(int,file.readline().split())
    sinkArray = file.readline().split()

    for i in range(int(roads)):
        a,b,c = map(int,file.readline().split())
        adArray[a][b] = c

    file.close()

    return adArray,sourceNum,sinkNum,sourceArray,sinkArray

def compPath(node,edge,i,paths):
    for path in paths:
        if int(path[1]) == node:
            print("starting node: "+str(path[0])+" second node: "+ str(node) +" ending node: "+ str(i))

def BFS(adArray,queue,sinkArray,paths):
    newQueue = []
    for node in queue:
        i=0
        for edge in adArray[node]:
            if edge>0:
                paths.append([node,i,edge])
                if str(i) in sinkArray:
                    print("here we calculate the path")
                    compPath(node,edge,i,paths)
                else:
                    newQueue.append(i)
            i+=1
    if newQueue.__len__()>0:
        BFS(adArray,newQueue,sinkArray,paths)
    print(paths)

if __name__ == "__main__":
    adArray, sourceNum, sinNum, sourceArray, sinkArray = MatrixMaker()
    print(adArray)
    print(sinkArray)
    print(sourceArray)
    paths = []
    BFS(adArray,sourceArray,sinkArray,paths)
    print(sinkArray)
