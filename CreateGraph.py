# the follwing class creates adjugate matrix to represent the undirected graph 
print("Please enter the amount of nodes:")
nodes = int(input())
if nodes <= 1:
    print('\033[91m' + "It is not possible to use only one node in the following simulation!" + '\033[0m')
    exit()
print("Please enter the amount of edges:")
edges = int(input())
# ToDo:The following values should be introduced to the graph
# print("Please enter the amount of infected:")
# infected = int(input())
# print("Please enter the infaction rate from 0 to 1:")
# rate = float(input())
print("Please enter nodes connectios, consider that the first node is 0:")

# Not sure if it is needed to print the matrix
def createMatrix(matrix):
    print("The graph will look as followed:")
    r,c = len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()

matrix = [[0]*nodes for i in range(nodes)]
for i in range(edges):
    u,v = map(int,input().split())
    matrix[u][v] = 1

createMatrix(matrix)

#Test case to check if the matrix is working, uncomment and enter as the input.
# 2 2
# A B
# B A