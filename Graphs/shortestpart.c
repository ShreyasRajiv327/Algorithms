#include <stdio.h>

int main() {
    int vertices;
    int A[10][10];
    int edges;
    scanf("%d", &vertices);
    scanf("%d", &edges);

    if (vertices == 0) {
        printf("-1");
        return 0;
    }

    if (vertices == 1) {
        int temp;
        scanf("%d", &temp);
        printf("%d", temp);
        return 0;
    }

    for (int i = 0; i < vertices; i++) {
        for (int j = 0; j < vertices; j++) {
            A[i][j] = 0; 
        }
    }

    int temp1, temp2;
    for (int j = 0; j < edges; j++) {
        scanf("%d, %d", &temp1, &temp2);
        A[temp1 - 1][temp2 - 1] = 1;
    }

    int s1,s2;

    scanf("%d, %d", &s1, &s2);
    int visited[vertices];
    int queue[vertices];
    int front = 0, rear = 0;
    int distance[vertices];

    for (int i = 0; i < vertices; i++) {
        visited[i] = 0;
        distance[i] = -1;
    }

    queue[rear++] = s1 - 1;
    visited[s1 - 1] = 1;
    distance[s1 - 1] = 0;

    while (front < rear) {
        int currentVertex = queue[front++];
        if (currentVertex == s2 - 1) {
            break;
        }

        for (int i = 0; i < vertices; i++) {
            if (A[currentVertex][i] == 1 && !visited[i]) {
                queue[rear++] = i;
                visited[i] = 1;
                distance[i] = distance[currentVertex] + 1;
            }
        }
    }

    if (distance[s2 - 1] == -1) {
        printf("-1");
    } else {
        printf("%d\n", distance[s2 - 1]);
    }

    return 0;
}