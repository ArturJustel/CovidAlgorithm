import sys
import struct

#this function reads the test file and assigns it the variables and makes the adjencecy matrix for the algoirithm to follow
def MatrixMaker():

    file = open('samples-A/2.in', 'r')
    #file = sys.stdin

    cities, roads = file.readline().split()
    print('cities: '+str(cities)+' roads: '+str(roads))

    adArray = [[0 for i in range(int(cities))] for j in range(int(cities))]

    sourceNum , sinNum = file.readline().split()

    sourceArray = file.readline()
    sinkArray = file.readline()

    print(adArray)
    print(sourceArray,end='')
    print(sinkArray,end='')

    for i in range(int(roads)):
        a,b,c = file.readline().split()
        adArray[int(a)][int(b)] = int(c)

    print(adArray)

    file.close()


if __name__ == "__main__":
    MatrixMaker()