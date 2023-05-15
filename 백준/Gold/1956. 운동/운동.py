import sys
input = sys.stdin.readline

V,E = map(int,input().split())
graph = [list(float('inf') for _ in range(V+1)) for _ in range(V+1)]
answer = float('inf')

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(1+V):
    graph[i][i] = 0

for k in range(1,1+V):
    for i in range(1,1+V):
        for j in range(1,1+V):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,1+V):
    for j in range(i+1,1+V):
        if graph[i][j] != float('inf') and graph[i][j]+graph[j][i] < answer:
            answer = graph[i][j]+graph[j][i]

if answer == float('inf'):
    print(-1)
else:
    print(answer)