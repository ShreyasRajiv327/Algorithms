def merge_sort(arr):
    comparisons = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        comparisons_left, left_half = merge_sort(left_half)
        comparisons_right, right_half = merge_sort(right_half)
        comparisons += comparisons_left + comparisons_right

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return comparisons, arr

# Input processing
size = int(input())
if size == 0:
    print(-1)
else:
    elements = list(map(int, input().split()))

    # Perform merge sort
    comparisons, sorted_array = merge_sort(elements)

    # Output the results
    print(comparisons)
    print(*sorted_array)

