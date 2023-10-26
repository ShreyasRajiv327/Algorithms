def merge(A1,A2,L):
    print("This is A1 LIST::",A1)
    print("This is A2 LIST::",A2)
    i=j=k=0
    while(i<len(A1) and j<len(A2)):
        if(A1[i]<A2[j]):
            L[k]=A1[i]
            i=i+1
            k=k+1
        else:
            L[k]=A2[j]
            j=j+1
            k=k+1
    while(i<len(A1)):
        L[k]=A1[i]
        i=i+1
        k=k+1
    while(j<len(A2)):
        L[k]=A2[j]
        j=j+1
        k=k+1
        
def mergesort(L):
    print("The list coming inside the function::",L)
    if len(L)>1:
        mid=len(L)//2
        A1=L[:mid]
        A2=L[mid:]
        mergesort(A1)
        print("The A1 List::",A1)
        mergesort(A2)
        print("The A2 List::",A2)
        merge(A1,A2,L)
def main():
    
    L=[10,1,89,14,39,2,23,34,100]
    mergesort(L)
    print(L)
main()