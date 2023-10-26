def insertionsort(L):
    for i in range(1,len(L)):
        j=i-1
        x=L[i]
        while(j>=0 and L[j]>x):
            L[j+1]=L[j]
            j=j-1
        L[j+1]=x
    print(L)        
def main():
    L=[10,16,8,12,15,6,3,9,5]
    insertionsort(L)
main()