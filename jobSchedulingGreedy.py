n = int(input("Enter number of jobs : "))
l = []
d = []
for i in range(n):
    temp = []
    temp.append(i+1)
    temp.append(int(input(f"Deadline of J{i+1} : ")))
    temp.append(int(input(f"Profit of J{i+1} : ")))
    l.append(temp)
    d.append(temp)
l.sort(key=lambda x:x[2],reverse=True)
d.sort(key=lambda x:x[1],reverse=True)
gantt = [0]*d[0][1]
profit = 0
for i in range(0,n):
    for j in range(l[i][1]-1,-1,-1):
        if gantt[j]==0:
            gantt[j]=f"J{l[i][0]}"
            profit+=l[i][2]
            break
print(gantt)
print(profit)