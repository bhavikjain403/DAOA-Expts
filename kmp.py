s = "_" + input("Enter the string : ")
p = "_" + input("Enter the pattern : ")
pi = [0]*(len(p))
for i in range(1,len(p)):
    for j in range(1,i):
        if p[i]==p[j]:
            pi[i]=j
print("The pi-table is",pi[1:])
i=1
j=0
while i<=len(s):
    if j==len(p)-1:
        print(f"Pattern found at index {i-j-1} which is {s[i-j:i-j+len(p)-1]}")
        j=0
    elif i<len(s) and p[j+1]==s[i]:
        j+=1
        i+=1
    else:
        if j==0:
            i+=1
        else:
            j = pi[j]