import sys

#The following function creates an adjacency matrix to represent a directed graph.
def MatrixMaker():

    file = open('sample-A.2.in', 'r')
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

class Graph:
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph) 

    #The following function performs the breadth-first search algorithm on the adjacency matrix,
    # to find the shortest path.
    def BFS(self,s, t, parent): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
          
        # Create a queue for BFS 
        queue=[] 
          
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
           
         # Standard BFS Loop 
        while queue: 
  
            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
          
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False

    #The following function performs the Ford-Fulkerson Algorithm on the shortest path to find the maximum flow.
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow

#The following function combines obtained max flow values and returns the final max flow value.
def sumFlowValue(g,sourceArray,sinkArray):
    final_flow = 0
    for i in range(len(sourceArray)):
      max_flow =  g.FordFulkerson(sourceArray[i], sinkArray[i])
      final_max_flow = final_flow + max_flow
    return final_max_flow

if __name__ == "__main__":
    adArray, sourceNum, sinNum, sourceArray, sinkArray = MatrixMaker()
    print('matrix is:',adArray)
    print('source is:',sourceArray)
    print('sink is:',sinkArray)

    g = Graph(adArray)
    final_max_flow = sumFlowValue(g,sourceArray,sinkArray)
    print ("The maximum possible flow is",final_max_flow)