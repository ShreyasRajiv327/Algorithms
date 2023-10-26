#include <stdio.h>
#include <stdlib.h>

#define MAX_NODE 100

struct Node {
    int Vertex;
    struct Node* next;
};

typedef struct Node Node;

struct List {
    Node* head;
};

typedef struct List List;

List* adjList[MAX_NODE] = {0};

void addNode(int s, int d) {
    Node* temp, *src, *dst;
    if (adjList[s]->head == NULL) {
        src = (Node*)malloc(sizeof(Node));
        src->Vertex = s;
        src->next = NULL;
        adjList[s]->head = src;
    }
    dst = (Node*)malloc(sizeof(Node));
    dst->Vertex = d;
    dst->next = NULL;
    temp = adjList[s]->head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = dst;
}

int main() {
    int maxNode;
    printf("Enter the value for max_node: ");
    scanf("%d", &maxNode);

    if (maxNode <= 0 || maxNode > MAX_NODE) {
        printf("Invalid value for max_node. Please use a value between 1 and %d.\n", MAX_NODE);
        return 1; 
    }

    for (int i = 0; i < maxNode; i++) {
        adjList[i] = (List*)malloc(sizeof(List));
        adjList[i]->head = NULL;
    }

    int s, d;
    char addMore;

    do {
        printf("Enter source and destination vertices (e.g., 0 1): ");
        scanf("%d %d", &s, &d);
        addNode(s, d);

        printf("Do you want to add more nodes (y/n)? ");
        scanf(" %c", &addMore); 

    } while (addMore == 'y' || addMore == 'Y');

    for (int i = 0; i < maxNode; i++) {
        Node* p = adjList[i]->head;
        printf("\nThe Adjacency list for vertex %d", i);
        while (p != NULL) {
            if (p->Vertex == i) {
                p = p->next;
            } else {
                printf("\n%d", p->Vertex);
                p = p->next;
            }
        }
        printf("\n");
    }

    return 0;
}
