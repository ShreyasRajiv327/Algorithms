def merge(L1,L2,L):
    comp = 0
    i=j=k=0
    while(i<len(L1) and j<len(L2)):
        comp += 1
        if(L1[i]<L2[j]):
            L[k]=L1[i]
            i += 1
            k += 1
        else:
            L[k]=L2[j]
            j += 1
            k += 1
    while(i<len(L1)):
        L[k]=L1[i]
        i += 1
        k += 1
    while(j<len(L2)):
        L[k]=L2[j]
        j += 1
        k += 1
    print(comp)
    print(" ".join(map(str,L)))
        
        
size1=int(input(""))
if size1 !=0 :
    L1=list(map(int,input("").split()))
else:
    L1=[]
size2=int(input(""))
if size2 !=0 :
    L2=list(map(int,input("").split()))
else:
    L2=[]
size=size1+size2
L=L1+L2
if size==0:
    print("-1")
else:
    merge(L1,L2,L)