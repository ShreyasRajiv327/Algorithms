#include<stdio.h>
#include<time.h>
#define size 100
int array[size];
void prime(int i)
{
    int j,c;
    for (j = 1; i <= j; j++) {
      if (i % j == 0) {
         c++;
      }
  }

  if (c == 2) {

        
  }
  else {
         printf("n is not a Prime number");
  }
}
int gcd(int a,int b)
{
  int i,j;
  for(i=1;i<=a;i++)
  {
    prime(i);

  }
}
void prime()
{

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