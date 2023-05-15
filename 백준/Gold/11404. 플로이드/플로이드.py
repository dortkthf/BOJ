import sys
from heapq import heappop, heappush

INF = int(1e9)

# 도시의 개수 n과 버스의 개수 m 입력
n = int(input())
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 버스 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 시작 도시에서 각 도시까지의 최소 비용을 저장할 리스트
cost = [[INF] * (n + 1) for _ in range(n + 1)]

# 다익스트라 알고리즘 함수
def dijkstra(start):
    # 시작 도시의 최소 비용은 0으로 설정
    cost[start][start] = 0

    # 우선순위 큐를 사용한 다익스트라 알고리즘
    heap = []
    heappush(heap, (0, start))

    while heap:
        dist, node = heappop(heap)

        # 이미 처리된 노드는 스킵
        if cost[start][node] < dist:
            continue

        # 인접한 도시들을 탐색
        for next_node, next_dist in graph[node]:
            new_cost = dist + next_dist

            # 현재까지의 최소 비용보다 더 작은 경우 갱신
            if new_cost < cost[start][next_node]:
                cost[start][next_node] = new_cost
                heappush(heap, (new_cost, next_node))

# 다익스트라 알고리즘을 모든 노드에 대해 실행
for i in range(1, n + 1):
    dijkstra(i)

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 도시 i에서 j로 가는 경로가 없는 경우 0 출력
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()
