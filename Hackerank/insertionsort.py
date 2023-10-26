size=int(input(""))
if size==0:
    print("-1")
else:
    L=list(map(int,input("").split()))
    comp=0
    movments=0
    for i in range(1,len(L)):
        j=i-1
        x=L[i]
        comp += 1
        while(j>=0 and L[j]>x):
            if(j==0):
                comp -= 1
            L[j],L[j+1]=L[j+1],L[j]
            comp += 1
            movments += 1
            j=j-1
        L[j+1]=x
        #movments += 1
    print(comp)
    print(movments)
    for ele in L:
        print(ele,end=" ")
        