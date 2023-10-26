def insertionsort(L):
    count=0
    swap=0
    for i in range(1,len(L)):
        j=i-1
        x=L[i]
        count=count+1
        while(j>=0 and L[j]>x):
            if(j==0):
                count=count-1#this is because when j==0 it is compaing with itself
            count=count+1
            #print("Value of L[j+1]::",L[j+1])
            #print("Value of L[j]::",L[j])
            L[j+1]=L[j]
            swap=swap+1
            #print("After Swap::",L)
            j=j-1
        #print("Value of X which is going to be placed in L[j+1]::",x)
        L[j+1]=x
        #swap=swap+i
        #print(L)
    print(count)
    print(swap)
    print(L)
            
        
 
            
def main():
    L=[5,4,3,2,1]
    insertionsort(L)
main()