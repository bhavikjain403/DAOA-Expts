def minmax(arr):
    while len(arr)>2:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        minmax(left)
        minmax(right)
        minl = min(left)
        maxl = max(left)
        maxr = max(right)
        minr = min(right)
        if minl>=minr:
            mini = minr
        else:
            mini = minl
        if maxl>=maxr:
            maxi = maxl
        else:
            maxi = maxr
        return mini, maxi

l = list(map(int, input("Enter the list of numbers : ").split()))
mini,maxi = minmax(l)
print(mini, maxi)