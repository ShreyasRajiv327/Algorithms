#include<stdio.h>
int count=0;
void TOH(int n,int A,int B,int C)
{
   if (n>0)
   {
      TOH(n-1,A,C,B);
      printf("\nMove disk from %d to %d",A,C);
      count++;
      TOH(n-1,B,A,C);
   }
}

int main()
{
    int n;
    printf("\nEnter the value of n:");
    scanf("%d",&n);
    int A=1;
    int B=2;
    int C=3;
    TOH(n,A,B,C);
    printf("\nCOUNT IS :%d",count);
    return 0;
}