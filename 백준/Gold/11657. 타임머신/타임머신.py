import sys

INF = sys.maxsize

def bellman_ford(start, graph, n):
    # 시작 도시에서 다른 도시까지의 최단 시간을 저장하는 리스트
    times = [INF] * (n + 1)
    times[start] = 0

    # 간선 relaxation 수행
    for _ in range(n - 1):
        for u in range(1, n + 1):
            for v, weight in graph[u]:
                if times[u] != INF and times[u] + weight < times[v]:
                    times[v] = times[u] + weight

    # 음수 사이클 확인
    for u in range(1, n + 1):
        for v, weight in graph[u]:
            if times[u] != INF and times[u] + weight < times[v]:
                return [-1]

    return times[2:]

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = bellman_ford(1, graph, n)

for time in result:
    print(time if time != INF else -1)