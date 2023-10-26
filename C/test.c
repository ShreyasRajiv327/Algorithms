#include<stdio.h>
int main()
{
    int i;
    int n=10;
    for(i=1;i<=n;i=i*i)
    {
        //printf("\n%d",i);
        printf("\nDAA");
         int ar3[10];
    int i=0;
    int j=0;
    int k=0;
   while(i<5 && j<5)
   {
     if(ar1[i]<ar2[j])
     {
        ar3[k++]=ar1[i++];
     }
     else
     {
        ar3[k++]=ar2[j++];
     }
   }
   for(;i<5;i++)
   {
    ar3[k++]=ar1[i];
   }
   for(;j<5;j++)
   {
    ar3[k++]=ar2[j];
   }
   printf("\nSorted ARRAY:");
   for(int c=0;c<10;c++)
   {
    printf("\n%d",ar3[c]);
   }
    }
}