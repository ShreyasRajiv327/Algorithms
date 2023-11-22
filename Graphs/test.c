#include <stdio.h>
#include<stdbool.h>
#define inf 9999
int main()
{
    int adjMatrix[10][10];
    int selected[10]={0,0,0,0,0,0,0,0,0,0};
    
    int vertices;
    printf("Enter no of Vertices");
    scanf("%d",&vertices);
    int i,j;
    for(i=0;i<10;i++)
    {
        for(j=0;j<10;j++)
        {
            adjMatrix[i][j]=0;
        }
    }
    int node,neighbour,weight;
    node=-1;
    neighbour=-1;
    weight=-1;
    while(node !=-1 && neighbour !=-1 && weight != -1)
    {
        printf("\nEnter the root node:");
        scanf("%d",&node);
        printf("\nEnter the neighbour for the node:");
        scanf("%d",&neighbour);
        printf("\nEnter the weight between them");
        scanf("%d",&weight);
        adjMatrix[node][neighbour]=weight;
    }
    selected[0]=1;
    int x;
    int y;
    int ed=0;
    while(ed<vertices)
    {
          int min = inf;
          x = 0;
          y = 0;
          for(i=0;i<vertices;i++)
          {
            if(selected[i])
            {
                for(j=0;j<vertices;j++)
                {
                    if(!selected[j] && adjMatrix[i][j])
                    {
                        if(min>adjMatrix[i][j])
                        {
                            min=adjMatrix[i][j];
                            x=i;
                            y=j;
                        }
                    }
                }
            }
          }
       selected[y]=1;
       ed++;
    }


   



}