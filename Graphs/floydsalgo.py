def floyd_warshall(vertices, edges):
  
    graph = [[9999] * vertices for j in range(vertices)]

    for edge in edges:
        source, dest, weight = edge
        graph[source - 1][dest - 1] = weight

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

def print_shortest_paths(graph, vertices):
    for i in range(vertices):
        for j in range(vertices):
            if i != j:
                print(f"{i + 1} {j + 1} {graph[i][j]}")

def main():
    vertices = int(input())
    edges_count = int(input())

    if edges_count == 0:
        print(-1)
        return
    
    edges = []
    if edges_count==1:
        edge=int(input(""))
        edges.append(edge)
    else:
        for j in range(edges_count):
            edge = list(map(int, input().split()))
            edges.append(edge)

        shortest_paths = floyd_warshall(vertices, edges)
        print_shortest_paths(shortest_paths, vertices)

if __name__ == "__main__":
    main()
