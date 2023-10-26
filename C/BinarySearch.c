#include <stdio.h>
#define size 5
int array[size];
void sort()
{
  int j,k;
  for(k=0;k<size-1;k++)
  {
  for(j=0;j<size-1;j++)
  {
    int x=array[j];
    int y=array[j+1];
    if(array[j]>array[j+1])
    {
       array[j]=y;
       array[j+1]=x;
    }
  }
}
int i;
for(i=0;i<size;i++)
{
   printf("\n%d",array[i]);
}
}
void BinarySearch(int ele)
{
    int c;
    int start,mid,end;
    start=0;
    end=size;
    mid=size/2;
    printf("\nSize of mid: %d",mid);
    if(array[mid]==ele)
    {
      printf("\n Element found at %d position->",mid);
    }
    else
    {
    if (ele>mid)
    {
        start=mid+1;
    }
    else
    {
        end=mid;
    }
    for(start;start<end;start++)
        {
            if(array[start]==ele)
            {
             printf("\n Element found at %d position->",start);
             c=1;
             break;
            }
            else
            {
              c=0;
            }
        }
    }
    if(c==0)
    {
        printf("\nElement not found");
    }
}
int main()
{
    int i,ele;
    for(i=0;i<size;i++)
    {
      printf("\nElement to enter :");
      scanf("%d",&array[i]);
    }
   sort();
   printf("\nEnter element to be searched :");
   scanf("%d",&ele);
   BinarySearch(ele);
}