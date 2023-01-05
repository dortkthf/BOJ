import sys, math
input = sys.stdin.readline
t = int(input())
res = []
for _ in range(t):
    x,y = map(int,input().split())
    res.append(math.lcm(x,y))
print(*res, sep='\n')