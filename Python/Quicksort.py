def partition(L, l, h):
    swap = 0
    count = 0
    print("List while entering the partition:",L)
    pivot = L[h]  # Choose the last element as the pivot
    i = l - 1

    for j in range(l, h):
        count += 1
        print("Value of i",i,"and",j)
        if L[j] <= pivot:
            i += 1
            if i != j:  # Count only if elements at two different indices exchange
                print("Elements getting swapped are:",L[i],"and",L[j])
                print("Value of i",i,"and",j)
                print("List before swapping",L)
                L[i], L[j] = L[j], L[i]
                print("List after swapping",L)
                swap += 1
            

    L[i + 1], L[h] = L[h], L[i + 1]
    if i + 1 != h:  # Count only if elements at two different indices exchange
        swap += 1
    #count += 1
    print("List while exiting the partition:",L)
    return i + 1, swap, count

def quicksort(L, l, h):
    if l < h:
        j, swap, count = partition(L, l, h)
        left_swap, left_count = quicksort(L, l, j - 1)
        right_swap, right_count = quicksort(L, j + 1, h)
        return swap + left_swap + right_swap, count + left_count + right_count
    return 0, 0

def hacker_rank_format():
    n = int(input())
    L = list(map(int, input().split()))

    h = len(L) - 1
    l = 0
    total_swap, total_count = quicksort(L, l, h)

    print(total_count)
    print(total_swap)
    print(" ".join(map(str, L)))

if __name__ == "__main__":
    hacker_rank_format()
