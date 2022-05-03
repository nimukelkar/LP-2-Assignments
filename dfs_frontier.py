

class Graph:
    def __init__(self):
        self.Graph_nodes={
            0:[1,2],
            1:[0,3],
            2:[0,3],
            3:[1,2,4,5],
            4:[3],
            5:[3]
        }
        self.parents={}
        self.frontier=[]
        self.closed=[]

    def retrace_path(self,current,start):
        path=[]
        while(self.parents[current]!=current):
            path.append(current)
            current=self.parents[current]
        path.append(start)
        path.reverse()
        print("The dfs path is",path)
        return

    def dfs(self,current):
        print("Current=",current)

        for n in self.Graph_nodes[current]:
            if(n not in self.frontier and n not in self.closed):
                self.parents[n]=current
                self.frontier.append(n)
                self.dfs(n)
        self.frontier.remove(current)
        self.closed.append(current)
        return
g1=Graph()
start=0
g1.frontier.append(start)
g1.parents[start]=start
g1.dfs(start)

destination=5
g1.retrace_path(destination,start)



