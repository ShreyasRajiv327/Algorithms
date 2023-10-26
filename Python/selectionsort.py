def selectionsort(L,size):
    count=0
    swap=0
    for i in range(0,size):
        min=i
        for j in range(i+1,size):
            count=count+1
            if L[min]>L[j]:
                min=j
            if min !=i:
                L[i],L[min]=L[min],L[i]
                swap=swap+1
    print(swap)
    print(count)
    print(" ".join(map(str, L)))



def main():
    size=int(input())
    if size==0:
        print("-1")
    elif size==1:
        L=list(map(int, input().split()))
        print(L[0])
    else:
        L=list(map(int, input().split()))
        selectionsort(L,size)
main()
