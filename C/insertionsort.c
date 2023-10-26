#include<stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int L[n];
    int i;
    for(i=0;i<n;i++)
    {
        scanf("%d",&L[i]);
    }
    int count =0;
    int swap=0;
    int j;
    for(i=1;i<n;i++)
    {
        j=i-1;
        int x=L[i];
        count++;
        while(j>=0 && L[j]>x)
        {
            if(j==0)
            {
                count--;
            }
            L[j+1]=L[j];
            j=j-1;
            swap++;
            count++;
        }
        L[j+1]=x;
    }
    printf("%d",count);
    printf("\n%d",swap);
    printf("\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",L[i]);
        
    }
    return 0;
}