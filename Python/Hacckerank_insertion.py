
def insertionsort(L):
    comp=0
    mov=0
    for i in range(1,len(L)):
        j=i-1
        x=L[i]
        while(j>=0 and L[j]>x):
            if j==0:
                comp=comp-1
            comp=comp+1
            L[j+1]=L[j]
            mov=mov+1
            j=j-1
        L[j+1]=x
        #mov=mov+1
    print(comp)
    print(mov)
def main():
    size=int(input())    
    if size==0:
        print(-1)
    elif size==1:
        L=[1]
        print(" ".join(map(str, L)))
        insertionsort(L)
    else:
        L=list(map(int,input("").split()))
        insertionsort(L)
        print(" ".join(map(str, L)))
    
main()