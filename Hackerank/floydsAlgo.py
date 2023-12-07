vertices = int(input(""))
edges = int(input(""))
if vertices==0:
    print("0")
elif vertices==1:
    edge=int(input(""))
    print(edge)
else:
     adj = [[9999] * vertices for _ in range(vertices)]
     for k in range(edges):
        input_str = input("")
        v1, v2, w = map(int, input_str.split())
        adj[v1 - 1][v2 - 1] = w
        
     for i in range(vertices):
         for j in range(vertices):
             for k in range(vertices):
                 adj[i][j]=min(adj[i][j],adj[i][k]+adj[k][j])
     for i in range(vertices):
         for j in range(vertices):
             for k in range(vertices):
                 if i != j:
                     print(f"{i+1} {j+1} {adj[i][j]}")