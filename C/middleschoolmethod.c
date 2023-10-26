#include<stdio.h>
#include<time.h>
int gcd(int a,int b)
{
  int i;
  for(i=0;i<=a;i++)
  {

  }
}
int main()
{
    clock_t t;
    t = clock();
    int a,b;
    printf("\nEnter 2 numbers to find gcd:");
    scanf("\n%d%d",&a,&b);
    int ans=gcd(a,b);
    t=clock()-t;
    printf("\nGCD IS %d",ans);
    printf("\nTime taken in seconds : %f",((double)t)/CLOCKS_PER_SEC);
}