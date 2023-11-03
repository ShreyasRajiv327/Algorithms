def depth_first_search(adj_matrix, start_vertex):
    num_vertices = len(adj_matrix)
    visited = [0] * num_vertices
    stack = [start_vertex]

    print("DFS Traversal starting from vertex", start_vertex)

    while stack:
        current_vertex = stack.pop()
        if visited[current_vertex]==0:
            print(current_vertex, end=" ")
            visited[current_vertex] = 1

        for vertex in range(num_vertices - 1, -1, -1):
            if adj_matrix[current_vertex][vertex] == 1 and not visited[vertex]:
                stack.append(vertex)

adjacency_matrix = [
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start_vertex = 0
depth_first_search(adjacency_matrix, start_vertex)
