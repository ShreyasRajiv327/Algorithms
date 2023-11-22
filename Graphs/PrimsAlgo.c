#include <stdio.h>
#include <stdbool.h>
#include <limits.h>  // Include limits.h for INT_MAX
#include <string.h>
#define V 5

int G[V][V] = {
    {0, 9, 75, 0, 0},
    {9, 0, 95, 19, 42},
    {75, 95, 0, 51, 66},
    {0, 19, 51, 0, 31},
    {0, 42, 66, 31, 0}
};

int main() {
    int no_edge = 0;
    int selected[V];
    int min, x, y;

    memset(selected, false, sizeof(selected));

    selected[0] = true;

    printf("Edge : Weight\n");

    while (no_edge < V - 1) {
        min = INT_MAX;  // Initialize min with a large value

        for (int i = 0; i < V; i++) {
            if (selected[i]) {
                for (int j = 0; j < V; j++) {
                    if (!selected[j] && G[i][j]) {
                        if (G[i][j] < min) {
                            min = G[i][j];
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }

        printf("%d - %d : %d\n", x, y, G[x][y]);
        selected[y] = true;
        no_edge++;
    }

    return 0;
}
