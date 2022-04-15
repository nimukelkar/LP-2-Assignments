
class Graph:

    def __init__(self):
        self.Graph_construct={
            'S': [('A', 3), ('B', 5)],
            'A': [('S', 3), ('B', 4), ('D', 3)],
            'B': [('S', 5), ('A', 4), ('C', 4)],
            'C': [('B', 4), ('E', 6)],
            'D': [('A', 3), ('G', 5)],
            'E': [('C', 6)],
            'G': [('D', 5)]
        }
        self.parent={}
        self.g={'S':100,'A':100,'B':100,'C':100,'D':100,'E':100,'G':100}
        self.frontier=[]
        self.closed=[]

    def reconstruct_path(self,current,start):
        l=[]
        cost=self.g[current]
        while(self.parent[current]!=current):
            l.append(current)
            current=self.parent[current]
        l.append(start)
        l.reverse()
        print("Path is",l)
        print("Cost is",cost)
        return l


    def astar(self,start):
        self.parent[start]=start
        self.g[start]=0
        self.frontier.append(start)
        #Step 1. Find the current node.

        while(self.frontier):
            current = None
            min = 1000
            for v in self.frontier:
                if(self.g[v]<min):
                    min=self.g[v]
                    current=v
        #Step 2 Expand frontier nodes and update gscore if necessary.
            for n,weight in self.Graph_construct[current]:
                g_tentative=self.g[current]+weight
                if(g_tentative<self.g[n]):
                    self.parent[n]=current
                    self.g[n]=g_tentative
                    self.frontier.append(n)
        #Remove current from frontier list
            self.frontier.remove(current)
            self.closed.append(current)
        return

g1=Graph()
start='S'
dest='G'
g1.astar(start)
print(g1.g)
print("Path taken is",g1.reconstruct_path(dest,start))



