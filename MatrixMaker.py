import sys
import struct

#this function reads the test file and assigns it the variables and makes the adjencecy matrix for the algoirithm to follow

def MatrixMaker():

    file = open('samples-A/1.in', 'r')
    #file = sys.stdin

    cities, roads = map(int,file.readline().split())

    adArray = [[0 for i in range(cities)] for j in range(cities)]

    sourceNum , sinkNum = map(int,file.readline().split())

    sourceArray = file.readline().split()
    sinkArray = file.readline().split()

    for i in range(int(roads)):
        a,b,c = map(int,file.readline().split())
        adArray[a][b] = c

    file.close()

    return adArray,sourceNum,sinkNum,sourceArray,sinkArray

def BSF(adArray,queue,sinkArray):
    newQueue = []
    for node in queue:
        print(node)
        i=0
        for edge in adArray[int(node)]:
            if edge>0:
                newQueue.append(i)
            i+=1
    print(newQueue)
    if newQueue.__len__()>0:
        BSF(adArray,newQueue,sinkArray)

if __name__ == "__main__":
    adArray, sourceNum, sinNum, sourceArray, sinkArray = MatrixMaker()
    print(adArray)
    BSF(adArray,sourceArray,sinkArray)
