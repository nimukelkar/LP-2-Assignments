

class Graph:
    def __init__(self):
        self.construct_graph={
            'S':[('A',3),('B',5)],
            'A':[('S',3),('B',4),('D',3)],
            'B':[('S',5),('A',4),('C',4)],
            'C':[('B',4),('E',6)],
            'D':[('A',3),('G',5)],
            'E':[('C',6)],
            'G':[('D',5)]
        }
        self.parent={}
        self.g={'S':100,'A':100,'B':100,'C':100,'D':100,'E':100,'G':100}
        self.frontier=[]
        self.closed=[]
    def reconstruct_path(self,node,start):
        l=[]
        cost=self.g[node]
        while(self.parent[node]!=start):
            l.append(node)
            node=self.parent[node]

        l.append(start)
        l.reverse()
        print("Path",l)
        print("minimum cost is",cost)
        return l




    def djikstra(self,start):
        self.parent[start]=start
        self.g[start]=0
        self.frontier.append(start)

        while(self.frontier):
            # Get current node as minimum g value(minimum accumulated cost from start) among frontier list
            current=None
            min=10000
            for v in self.frontier:
                if(self.g[v]<min):
                    min=self.g[v]
                    current=v
            #Expand the current.Update g
            for n,cost in self.construct_graph[current]:
                g_tentative=self.g[current]+cost
                if(g_tentative<self.g[n]):
                    self.parent[n]=current
                    self.g[current]=g_tentative
                    self.frontier.append(n)
            #Remove current from frontier list, transfer to closed list.
            self.frontier.remove(current)
            self.closed.append(current)
        return
g1=Graph()
start='S'
dest='B'
g1.djikstra(start)
print("Minimum cost dictionary is",g1.g)
print("Path traced is",g1.reconstruct_path(dest,start))







