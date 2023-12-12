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
    dist=[0]*vertices
    visited=[0]*vertices
    for i in range(vertices):
        dist[i]=adj[0][i]
    visited[0]=1
    n=0
    while(n<vertices-1):
        min_edge=9999
        for j in range(vertices):
            if dist[j]<min_edge and not visited[j]:
                min_edge=dist[j]
                v=j
        visited[v]=1
        for k in range(vertices):
            if(dist[k]>dist[v]+adj[v][k]):
                dist[k]=dist[v]+adj[v][k]
        n += 1
    for y in range(1,len(dist)):
        print(f"1 {y+1} {dist[y]}")
                