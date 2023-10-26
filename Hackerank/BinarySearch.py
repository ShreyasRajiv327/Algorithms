def Binarysearch(L,k):
    high=len(L)-1
    low=0
    comparison=0
    while(low<=high):
        comparison += 1
        mid=(low+high)//2
        if L[mid]==k:
            return comparison,mid
        else:
            if L[mid]>k:
                high=mid-1
            else:
                low=mid+1
    return comparison,-1
n=int(input(""))
if n==0:
    print("-1")
else:
    L=list(map(int,input("").split()))
    k=int(input(""))
    comp,index=Binarysearch(L,k)
    print(comp)
    if index!=-1:
        print(index)
    else:
        print("-1")