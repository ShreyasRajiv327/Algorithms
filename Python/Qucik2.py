swap = 0  # Initialize the swap count

def partition(arr,l,h):
    pivot=arr[h]
    i=l-1
    for k in range(l,h-1):
        if(arr[k]<=pivot):
            i=i+1
            arr[i],arr[k]=arr[k],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

def quicksort(arr, left, right):
    if left < right:
        #pivot_index = right
        j = partition(arr, left, right)
        quicksort(arr, left, j - 1)
        quicksort(arr, j + 1, right)

data = [1 ,3, 9, 8 ,2, 7, 5]

size = len(data)

quicksort(data, 0, size - 1)

#print('Sorted Array in Ascending Order:')
print(data)
print(swap)  # Print the swap count after sorting
