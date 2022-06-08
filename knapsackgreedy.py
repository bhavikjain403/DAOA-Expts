n = int(input("Enter number of items : "))
m = int(input("Enter capacity of knapsack : "))
data = []
for i in range(n):
    temp = []
    temp.append(i+1)
    temp.append(int(input(f"Enter value of item {i+1} : ")))
    temp.append(int(input(f"Enter weight of item {i+1} : ")))
    temp.append(temp[1]/temp[2])
    data.append(temp)
data.sort(key=lambda x:x[3], reverse=True)
order = []
profit = 0
for i in range(0,n):
    if m==0:
        break
    elif m>=data[i][2]:
        profit+=data[i][1]
        order.append(f"Item{data[i][0]}")
        m-=data[i][2]
    elif m>0:
        frac = m/data[i][2]
        profit+=data[i][1]*frac
        order.append(f"Item{data[i][0]}*{round(frac,3)}")
        break
print("Profit is",round(profit,3))
print("Order is",order)