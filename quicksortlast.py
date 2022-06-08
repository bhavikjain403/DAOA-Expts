def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low<high:
        j=partition(arr,low,high)
        quicksort(arr,low,j-1)
        quicksort(arr,j+1,high)

l = list(map(int,input("Enter the list : ").split()))
n = len(l)
quicksort(l,0,n-1)
print("The sorted list is :",l)