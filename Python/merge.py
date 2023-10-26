def merge(A1, A2, L):
    i = j = k = 0
    comparisons = 0  # Initialize a variable to count comparisons
    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            L[k] = A1[i]
            i += 1
        else:
            L[k] = A2[j]
            j += 1
        k += 1
        comparisons += 1  # Count the comparison
    while i < len(A1):
        L[k] = A1[i]
        i += 1
        k += 1
    while j < len(A2):
        L[k] = A2[j]
        j += 1
        k += 1
    return comparisons  # Return the total number of comparisons

def mergesort(L):
    if len(L) > 1:
        mid = len(L) // 2
        A1 = L[:mid]
        A2 = L[mid:]
        comparisons_A1 = mergesort(A1)
        comparisons_A2 = mergesort(A2)
        comparisons_merge = merge(A1, A2, L)
        return comparisons_A1 + comparisons_A2 + comparisons_merge
    return 0

def main():
    L = [5,4,3,2,1]
    total_comparisons = mergesort(L)
    print("Sorted List:", L)
    print("Total Comparisons:", total_comparisons)

main()
