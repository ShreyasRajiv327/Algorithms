#include<stdio.h>
#include<stdlib.h>
#define max_node 100
struct node{
 int Vertex;
 struct node* next;
};
typedef struct node node;
struct list{
    node* head;
};
typedef struct list list;
list* adjlist[max_node]={0};
void addnode(int s,int d){
    node *temp,*src,*dst;
    if(adjlist[s]->head==NULL)
    {
        src=(node*)malloc(sizeof(node));
        src->Vertex=s;
        src->next=NULL;
        adjlist[s]->head=src;
    }
    dst=(node*)malloc(sizeof(node));
    dst->Vertex=d;
    dst->next=NULL;
    temp=adjlist[s]->head;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=dst;
}
int main()
{
    int i;
    for(i=0;i<max_node;i++)
    {
        adjlist[i]=(list*)malloc(sizeof(list));
        adjlist[i]->head=NULL;
    }
    addnode(0,1);
    addnode(0,3);
    addnode(1,2);
    for(i=0;i<max_node;i++)
    {
        node* p=adjlist[i]->head;
        printf("\nThe Adjacency list for vertex %d",i);
        while(p!=NULL)
        { 
            if(p->Vertex==i)
            {
              p=p->next;
            }
            else
            {
            printf("\n%d",p->Vertex);
            p=p->next;
            }

        }
        printf("\n");
    }
   return 0;
}