class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i]==i:
            return i
        return self.find(parent, parent[i])

    def applyUnion(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot]<rank[yroot]:
            parent[xroot]= yroot
        elif rank[xroot]>rank[yroot]:
            parent[yroot]= xroot
        else:
            parent[yroot]= xroot
            rank[xroot]+=1

    def kruskal(self):
        i,e=0,0
        result = []
        parent = []
        rank = []
        cost=0
        self.graph = sorted(self.graph, key = lambda x: x[2])
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e<self.V-1:
            u,v,w = self.graph[i]
            i+=1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x!=y:
                e+=1
                result.append([u,v,w])
                cost+=w
                self.applyUnion(parent, rank, x, y)
        print("MST is as follows :")
        for u,v,w in result:
            print(u,"--->",v,":",w)
        print("Cost is",cost)

n=int(input("Enter number of vertices : "))
g = Graph(n)
G = []
print("Enter adjacency matrix : ")
for i in range(n):
    G.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if G[i][j]:
            g.addEdge(i,j,G[i][j])
g.kruskal()