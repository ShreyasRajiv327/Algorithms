def bfs(adj_matrix, start_vertex):
    num_vertices = len(adj_matrix)
    visited = [0] * num_vertices
    queue = []

    visited[start_vertex] = 1
    queue.append(start_vertex)

    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex, end=" ")

        for vertex in range(num_vertices):
            if adj_matrix[current_vertex][vertex] == 1 and not visited[vertex]:
                visited[vertex] = 1
                queue.append(vertex)
adjacency_matrix = [
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start_vertex = 0
print("BFS Traversal starting from vertex", start_vertex)
bfs(adjacency_matrix, start_vertex)
