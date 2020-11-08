import sys

#this function reads the test file and assigns it the variables and makes the adjencecy matrix for the algoirithm to follow

def MatrixMaker():

    file = open('samples-A/1.in', 'r')
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

def compPath(node,sourceArray,paths):
    helpArray = list(reversed(paths))
    print(helpArray)
    helpArray = helpArray[1:]
    for path in helpArray:
        print("current path: ", path)
        print("begining list:", paths, " and the node we are looking for: ", node, "and the sink ", sinkArray)
        if path[0] in sourceArray and path[1] == node:
            print("found the shortest route: ", paths)
            return paths
        if path[1] == node:
            print("lets try again")
            compPath(path[0],sinkArray,paths)
        else:
            paths.remove(path)
            print("removed list: ", paths)

def BFS(adArray,queue,sinkArray,paths,visited):
    newQueue = []
    for node in queue:
        i=0
        for edge in adArray[node]:
            if edge>0:
                paths.append([node,i,edge])
                if i in sinkArray:
                    print("here we calculate the path")
                    shortestPath = compPath(node,sourceArray,paths)
                    print("shortestPathBFS :",shortestPath)
                    return shortestPath
                elif i in visited:
                    print("visited")
                    continue
                else:
                    newQueue.append(i)
            i+=1
    if newQueue.__len__()>0:
        BFS(adArray,newQueue,sinkArray,paths,visited)
    print(paths)

if __name__ == "__main__":
    adArray, sourceNum, sinNum, sourceArray, sinkArray = MatrixMaker()
    visited = sourceArray
    paths = []
    shortestPath = BFS(adArray,sourceArray,sinkArray,paths,visited)
    print("shortestPathmain: ", shortestPath)
