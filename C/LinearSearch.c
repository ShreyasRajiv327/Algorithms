#include <stdio.h>
#define size 5
int array[size];
void linearSearch(int ele)
{
    int j,k;
    for(j=0;j<size;j++)
    {
     if(array[j]==ele)
     {
        printf("\nElement %d is in the positon: %d",ele,j);
        k=1;
        break;

     }
     else 
     {
        k=0;
     }
    }
    if(k==0)
    {
        printf("\nElement not found");
    }
  
}
int main()
{
    int i,ele;
    for(i=0;i<size;i++)
    {
      printf("\nElement to enter");
      scanf("%d",&array[i]);
    }
   printf("\nEnter element to be searched");
   scanf("%d",&ele);
   linearSearch(ele);
}