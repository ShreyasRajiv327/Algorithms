vertices = int(input(""))
edges = int(input(""))
if vertices==0 and edges==0:
    print("-1")
else:
    adj = [[9999] * vertices for _ in range(vertices)]
    for k in range(edges):
        input_str = input("")
        v1, v2, w = map(int, input_str.split())
        adj[v1 - 1][v2 - 1] = w
        #adj[v2 - 1][v1 - 1] = w  # Since the graph is undirected
    selected = [0] * vertices
    selected[0] = 1
    n = 0
    mst = 0
    while n < vertices - 1:
        min_edge = 9999
        u = -1
        v = -1
        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and adj[i][j] != 9999:
                        if adj[i][j] < min_edge:
                            min_edge = adj[i][j]
                            u = i
                            v = j

        if u != -1 and v != -1:
            selected[v] = 1
            n += 1
            mst += min_edge
    print(mst)

