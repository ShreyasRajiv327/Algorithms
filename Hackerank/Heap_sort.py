def heapify(arr, n, i, swap_count):
    largest = i
    #print("Largest array",arr[largest])
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
        #swap_count += 1

    if r < n and arr[largest] < arr[r]:
        largest = r
        #swap_count += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swap_count += 1
        swap_count = heapify(arr, n, largest, swap_count)
    #print(swap_count)
    return swap_count

def heapSort(arr):
    n = len(arr)
    swap_count = 0

    for i in range(n//2 - 1, -1, -1):
        print("Value of n:",n//2 - 1)
        swap_count = heapify(arr, n, i, swap_count)
    print("Array after heapify:",arr)
    for i in range(n-1, 0, -1):
        print("Value of I:",i)
        print("Before inital swap",arr)
        arr[i], arr[0] = arr[0], arr[i]
        print("After inital swap",arr)
        swap_count += 1
        #print("The array before sorting:",arr)
        swap_count = heapify(arr, i, 0, swap_count)
        print("After heapifying for sort:",arr)

    return swap_count

# Input
size = int(input().strip())
if size == 0:
    print(-1)
else:
    elements = list(map(int, input().strip().split()))

    # Sorting
    swaps = heapSort(elements)

    # Output
    print(swaps)
    print(" ".join(map(str, elements)))
