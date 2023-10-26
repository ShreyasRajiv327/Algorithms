#include<stdio.h>

int ar1[5]={1,3,5,7,9};
int ar2[5]={2,4,6,8,10};

void merge(){
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
int main()
{
    merge();
}
