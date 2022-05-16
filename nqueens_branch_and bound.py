

class NQueens:
    def __init__(self):
        self.n=4
        self.value=[0,1,2,3]
        self.frontier=[]
        self.closed=[]


    def checkprev(self,current,index,c):
        for v in range(index):
            if(current[v]==c):
                return False
            if(v-index==current[v]-c):
                return False
            if(index-v==current[v]-c):
                return False
        return True




    def bfs(self):
        self.frontier.append([])

        while(self.frontier):
            current=self.frontier.pop(0)# First list of frontier which is a list of lists.

            if(len(current)==self.n):
                print("Full solution found")
                print(current)
            for c in self.value:
                index=len(current)
                if(self.checkprev(current,index,c)):
                    new=current.copy()
                    new.append(c)
                    self.frontier.append(new)
        return
n1=NQueens()
n1.bfs()
