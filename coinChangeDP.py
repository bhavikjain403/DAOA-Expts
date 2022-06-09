from matplotlib.pyplot import table


amt = int(input("Enter the amount : "))
d = list(map(int, input("Enter the list of coin denominations : ").split()))
n = len(d)
table = []
ans = []
for i in range(n+1):
    table.append([0]*(amt+1))
d.append(0)
d.sort()
for i in range(1,n+1):
    for j in range(1, amt+1):
        if i==1 and j<d[i]:
            table[i][j]=99999999
        elif i==1:
            table[i][j] = 1 + table[i][j-d[i]]
        elif j<d[i]:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = min(table[i-1][j], 1 + table[i][j-d[i]])

while j>0:
    if table[i][j]==table[i-1][j]:
        i-=1
    else:
        j-=d[i]
        ans.append(d[i])
print("The table is as follows :")
for i in range(n+1):
    for j in range(amt+1):
        print(f"{table[i][j]}\t",end="")
    print("")
print(ans)