#include <stdio.h>
#include <stdlib.h>

struct node {
    int vertex;
    struct node* next;
};

struct Graph {
    int numVertices;
    struct node** adjLists;
};

struct node* createNode(int v) {
    struct node* newNode = malloc(sizeof(struct node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

struct Graph* createGraph(int vertices) {
    struct Graph* graph = malloc(sizeof(struct Graph));
    graph->numVertices = vertices;
    graph->adjLists = malloc(vertices * sizeof(struct node*));

    int i;
    for (i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;

    return graph;
}

void addEdge(struct Graph* graph, int s, int d) {
    // Add edge from s to d
    struct node* newNode = createNode(d);
    newNode->next = graph->adjLists[s];
    graph->adjLists[s] = newNode;

    // Add edge from d to s (for undirected graph)
    newNode = createNode(s);
    newNode->next = graph->adjLists[d];
    graph->adjLists[d] = newNode;
}

void printAdjacentVertices(struct Graph* graph, int vertex) {
    if (vertex < 0 || vertex >= graph->numVertices) {
        printf("-1\n");
        return;
    }

    struct node* temp = graph->adjLists[vertex];
    if (!temp) {
        printf("-1\n");
        return;
    }

    int first = 1; // To handle comma separation
    while (temp) {
        if (!first) {
            printf(",");
        }
        printf("%d", temp->vertex);
        first = 0;
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    int numVertices;
    scanf("%d", &numVertices);

    if (numVertices == 0) {
        printf("-1\n");
        return 0;
    } else if (numVertices == 1) {
        int singleVertex;
        scanf("%d", &singleVertex);
        printf("%d\n", singleVertex);
        return 0;
    }

    struct Graph* graph = createGraph(numVertices);

    int s, d;
    while (scanf("%d", &s) == 1 && s != -1) {
        scanf("%d", &d);
        addEdge(graph, s, d);
    }

    int queryVertex;
    scanf("%d", &queryVertex);
    printAdjacentVertices(graph, queryVertex);

    return 0;
}
