# the follwing class creates adjugate matrix to represent the undirected graph 
print("Please enter the amount of cities and roads:")
n,m = map(int, input().split()) 
if n <= 1 & m < 1: # ToDo: We should add the check for cities at least 30000 and roads 100000. 
    print('\033[91m' + "It is not possible to use such a small variables for the following simulation!" + '\033[0m')
    exit()
print("Please enter the amount of endangered cities and the amount of disignated:")
e,d = map(int, input().split())
if (e+d) > n : # check that e + d ≤ n 
    print('\033[91m' + "The amount of cities in use is more than declared!" + '\033[0m')
    exit()

# ToDo:The following values should be introduced to the graph
# print("Please enter the list of endangered cities by using 0-based indices of the corresponding cities:") # This can be seen as S
# print("Please enter the list of disignated cities by using 0-based indices of the corresponding cities:") # This can be seen as T
print("Please enter roads connectios and its capacity:")

# Not sure if it is needed to print the matrix
def createMatrix(matrix):
    print("The graph will look as followed:")
    r,c = len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()

matrix = [[0]*n for i in range(n)]
for i in range(m):
    u,v,c = map(int,input().split()) # ToDo: Impliment the c value
    matrix[u][v]= 1
    

createMatrix(matrix)

#Test case to check if the matrix is working, uncomment and enter as the input.
# 2 2 
# 0 1 100
# 1 0 100