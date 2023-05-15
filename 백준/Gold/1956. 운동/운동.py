import sys
input = sys.stdin.readline

V,E = map(int,input().split())
graph = [list(sys.maxsize for _ in range(V+1)) for _ in range(V+1)]
answer = sys.maxsize

for _ in range(E):
    a,b,c = map(int,input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for i in range(1+V):
    for j in range(1+V):
        if i == j:
            graph[i][j] = 0

for k in range(1,1+V):
    for i in range(1,1+V):
        for j in range(1,1+V):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,1+V):
    for j in range(i+1,1+V):
        if graph[i][j] != sys.maxsize and graph[i][j]+graph[j][i] < answer:
            answer = graph[i][j]+graph[j][i]

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)