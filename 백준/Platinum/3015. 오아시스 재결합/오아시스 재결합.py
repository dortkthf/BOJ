import sys

input = sys.stdin.readline
n = int(input())
stack = []
res = 0

for _ in range(n):
    now = int(input())
    cnt = 1

    while stack and stack[-1][0] <= now:
        height, cnt = stack.pop()
        if height == now:
            res += cnt
            cnt += 1
        elif height < now:
            res += cnt
            cnt = 1

    if stack:
        res += 1
    stack.append((now, cnt))

print(res)