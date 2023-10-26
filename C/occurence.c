#include<stdio.h>
#define SIZE 5
int array[SIZE];
void  search()
{
    int x;
    int i;
    int y;
    int count = 0;
    for(i=0;i<SIZE;i++)
    {
        x=array[i];
        for(y=0;y<SIZE;y++)
        {
            if(x==array[y])
            {
              count++;
            }
        }
        printf("\nOccurence of the number of %d is %d",array[i],count);
        count=0;
        if(array[i]==array[i+1])
        {
            i= i+1;
        }
    }
}
int main()
{
    int ele;
    int i;
    printf("Add elements to the array\n");
    for(i=0;i<SIZE;i++)
    {
        scanf("%d",&array[i]);
    }
   printf("\n*******");
   search();
   return 0;
   
}

