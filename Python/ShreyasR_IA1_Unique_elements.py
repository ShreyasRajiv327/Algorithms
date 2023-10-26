
def unique(L,n):
    unique=0
    count=0
    for i in range(0,n):
        c=L[i]
        for j in range(0,n):
            if L[j]==c:
                count=count+1
        if count==1:
            count=0
        else:
            unique=+1
    if unique==0:
        return 1
    else:
        return -1
def main():
    size=int(input())
    if size==0:
        print(0)
    else:
        L=list(map(int,input("").split()))
        ret=unique(L,size)
        print(ret)
    
main()