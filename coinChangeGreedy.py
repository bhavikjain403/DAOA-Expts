amt = int(input("Enter the amount : "))
l = list(map(int,input("Enter the available denomination of coins : ").split()))
l.sort(reverse=True)
coins = []
i=0
while i<len(l):
    if amt==0:
        break
    elif amt>=l[i]:
        amt-=l[i]
        coins.append(l[i])
    else:
        i+=1
print(coins)