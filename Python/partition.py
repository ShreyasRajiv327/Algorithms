def partition(L,pivot,l,h,swaps):
    x=L[pivot]
    i=l-1
    for j in range(l,h):
        if(L[j]<=x):
            i += 1
            if(L[j]!=L[i]):
                swaps[0] += 1
            L[i],L[j]=L[j],L[i]
    L[pivot],L[i+1]=L[i+1],L[pivot]
    swaps[0] += 1
    return i+1

def main():
    size=int(input(""))
    if size == 0:
        print("-1")
    else:
        L=list(map(int,input("").split()))
        pivot=int(input(""))
        swaps= [0]
        q=partition(L,pivot,0,size-1,swaps)
        print(swaps[0])
        print(" ".join(map(str, L)))
        print(q)
        
main()
