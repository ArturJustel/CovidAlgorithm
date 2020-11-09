import sys

#The following function creates an adjacency matrix to represent a directed graph.
def MatrixMaker():

    file = open('sample-A.1.in', 'r')
    # file = sys.stdin

    cities, roads = map(int,file.readline().split())
    adArray = [[0 for i in range(cities)] for j in range(cities)]
    sourceNum , sinkNum = map(int,file.readline().split())
    sourceArray = list(map(int,file.readline().split()))
    sinkArray = list(map(int,file.readline().split()))

    for i in range(int(roads)):
        a,b,c = map(int,file.readline().split())
        adArray[a][b] += c

    file.close()
    return adArray,sourceNum,sinkNum,sourceArray,sinkArray

class Graph:
    #The following method transformes the adjacency matrix into a graph to make further operations easier.
    def __init__(self,graph): 
        self.graph = graph
        self. ROW = len(graph) 

    #The following function performs the breadth-first search algorithm on the adjacency matrix,
    # to find the shortest path.
    def BFS(self,s, t, track_list): 
  
        visited_list =[False]*(self.ROW) 
        BFS_queue=[] 
        BFS_queue.append(s) 
        visited_list[s] = True
        #BFS loop   
        while BFS_queue: 
            u = BFS_queue.pop(0) 
            for ind, val in enumerate(self.graph[u]): 
                if visited_list[ind] == False and val > 0 : 
                    BFS_queue.append(ind) 
                    visited_list[ind] = True
                    track_list[ind] = u 
        return True if visited_list[t] else False

    #The following function performs the Ford-Fulkerson Algorithm on the shortest path to find the maximum flow.
    def FordFulkerson(self, source, sink): 
   
        track_list = [-1]*(self.ROW) 
        max_flow = 0
  
        while self.BFS(source, sink, track_list) : 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[track_list[s]][s]) 
                s = track_list[s] 
            max_flow +=  path_flow 
            v = sink 
            while(v !=  source): 
                u = track_list[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = track_list[v] 
        return max_flow

#The following function combines obtained max flow values and returns the final max flow value.
def sumFlowValue(graph,sourceArray,sinkArray):
    final_max_flow_value = 0
    for i in range(len(sourceArray)):
      max_flow =  graph.FordFulkerson(sourceArray[i], sinkArray[i])
      final_max_flow_value = final_max_flow_value + max_flow
    return final_max_flow_value

if __name__ == "__main__":
    adArray, sourceNum, sinNum, sourceArray, sinkArray = MatrixMaker()
    graph = Graph(adArray)
    final_max_flow_value = sumFlowValue(graph,sourceArray,sinkArray)
    sys.stdout.write(str(final_max_flow_value))