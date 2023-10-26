def partition(L, l, h):
    swap = 0
    count = 0

    pivot = L[l]
    i = l
    j = h

    while True:
        while L[i] < pivot:
            count += 1
            i += 1
        while L[j] > pivot:
            count += 1
            j -= 1
        if i >= j:
            return j, swap, count
        L[i], L[j] = L[j], L[i]
        swap += 1

def quicksort(L, l, h):
    if l < h:
        j, swap, count = partition(L, l, h)
        left_swap, left_count = quicksort(L, l, j)
        right_swap, right_count = quicksort(L, j + 1, h)
        return swap + left_swap + right_swap, count + left_count + right_count
    return 0, 0

def main():
    L = [1 ,3, 9, 8 ,2, 7, 5]
    h = len(L) - 1
    l = 0
    total_swap, total_count = quicksort(L, l, h)
    print(L)
    print("No of swappings:", total_swap)
    print("No of Comparisons:", total_count)

main()

