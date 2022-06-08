a = input("Enter first sequence : ")
b = input("Enter second sequence : ")
lcs = ""
table = []
for i in range(len(a)+1):
    table.append([0]*(len(b)+1))  
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            table[i][j]= 1 + table[i-1][j-1]
        else:
            table[i][j]= max(table[i-1][j], table[i][j-1])
i = len(a)
j = len(b)
while i>0 and j>0:
    if a[i-1]==b[j-1]:
        lcs+=a[i-1]
        i-=1
        j-=1
    elif table[i-1][j]>table[i][j-1]:
        i-=1
    else:
        j-=1
print("Number of characters in LCS is :",table[-1][-1])
print("The LCS is",lcs[::-1])