import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int,input().split())

graph = list([] for i in range(n+1))

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

check = [0 for i in range(n+1)]
res = []

queue = deque()
queue.append(r)

while queue:
    for i in graph[queue[0]]:
        if check[i] == 0:
            check[i] = 1
            queue.append(i)
    res.append(queue[0])
    check[queue.popleft()] = 1

cnt = 1
for i in res:
    check[i] = cnt
    cnt+=1

print(*check[1:], sep='\n')