def partition(L,l,h):
    pivot=L[h]
    i=l-1
    swap=0
    count=0
    for j in range(l,h):
        count += 1
        if L[j]<=pivot:
            i += 1
            if i!=j:
                L[i],L[j]=L[j],L[i]
                swap += 1
    L[i+1],L[h]=L[h],L[i+1]
    if i+1!=h:
        swap += 1
    return i+1,swap,count
def quicksort(L,l,h):
    if l<h:
        j,swap,count=partition(L,l,h)
        left_swap,left_count=quicksort(L,l,j-1)
        right_swap,right_count=quicksort(L,j+1,h)
        return swap+left_swap+right_swap,count+left_count+right_count
    return 0,0  

def main():
    n=int(input())
    L=list(map(int,input().split()))
    l=0
    h=len(L)-1
    total_swap,total_count=quicksort(L,l,h)
    print(total_count)
    print(total_swap)
    print(*L)
main()