INF = 999999999
n = int(input("Enter number of vertices : "))
print("Enter the adjacency matrix :")
G=[]
for i in range(n):
    G.append(list(map(int,input().split())))
selected = [0]*n
no_edges = 0
selected[0]=1
cost=0
print("The minimum spanning tree is as follows :")
while no_edges<(n-1):
    minimum = INF
    x=0
    y=0
    for i in range(0,n):
        if selected[i]:
            for j in range(0,n):
                if((not selected[j]) and G[i][j]):
                    if minimum>G[i][j]:
                        minimum=G[i][j]
                        x=i
                        y=j
    selected[y]=1
    no_edges+=1
    cost+=G[x][y]
    print(x,"---",y,":",G[x][y])
print("The minimum cost is",cost)