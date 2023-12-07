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
    for i in range(0,vertices):
        dist[i]=adj[0][i]
    visited[1-1]=1
    dist[1-1]=0
    n=0
    while(n<vertices):
        min=9999
        for j in range(1,vertices):
            if dist[j]<min and visited[j]==0:
                min=dist[i]
                v=j
        visited[v]=1
        for k in range(1,vertices):
            if(dist[k]>dist[v]+adj[v][k]):
                dist[k]=dist[v]+adj[v][k]
        n += 1
    print(dist)
                