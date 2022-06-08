sum = int(input("Enter the sum : "))
subset = list(map(int, input("Enter the subset : ").split()))
ans = []
def solve(s, idx):
    if s>sum:
        return
    if s==sum:
        print(ans)
        return
    i = idx
    while(i<len(subset)):
        ans.append(subset[i])
        solve(s+subset[i],i+1)
        ans.pop()
        i+=1
solve(0,0)