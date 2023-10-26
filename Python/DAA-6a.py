

def min(L,size):
    k=0
    c=L[k]
    for k in range(len(L)):
        if c>L[k]:
            c=L[k]
            num=k
    print(num)
    print(c)
        
    
    
    
def main():
    size=int(input())
    if size==0:
        print("-1")
    else:
        L=list(map(int,input("").split()))
        min(L,size)

main()