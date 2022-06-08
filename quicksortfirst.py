def partition(arr, start, high):
    pivot = arr[start]
    low = start +1
    while True:
        while low<=high and arr[low]<=pivot:
            low+=1
        while low<=high and arr[high]>=pivot:
            high-=1
        if low<=high:
            arr[low], arr[high]= arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high

def quicksort(arr,low,high):
    if low<high:
        j=partition(arr,low,high)
        quicksort(arr,low,j-1)
        quicksort(arr,j+1,high)

l = list(map(int,input("Enter the list : ").split()))
n = len(l)
quicksort(l,0,n-1)
print("The sorted list is :",l)