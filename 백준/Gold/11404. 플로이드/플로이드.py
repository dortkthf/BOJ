import collections, sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def min_price(number):
    queue = collections.deque()
    queue.append((number,0))
    price_list = list(sys.maxsize for _ in range(n+1))
    price_list[number] = 0

    while queue:
        start,sprice = queue.popleft()
        for i in graph[start]:
            end,eprice = i
            if price_list[start] != sys.maxsize and price_list[end] > sprice+eprice:
                price_list[end] = sprice+eprice
                queue.append((end,sprice+eprice))
    for i in range(1,n+1):
        if price_list[i] == sys.maxsize:
            price_list[i] = 0
    return price_list[1:]

for i in range(1,n+1):
    print(*min_price(i))