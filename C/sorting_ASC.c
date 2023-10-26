#include<stdio.h>
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
}

int main()
{
    int i,ele;
    for(i=0;i<size;i++)
    {
      printf("\nElement to enter");
      scanf("%d",&array[i]);
    }
    sort();
    for(i=0;i<size;i++)
    {
        printf("\n%d",array[i]);
    }
}
