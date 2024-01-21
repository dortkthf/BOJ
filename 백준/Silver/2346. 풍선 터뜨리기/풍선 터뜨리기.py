from collections import deque

n = int(input())
nums = list(map(int,input().split()))
bln = deque(list(enumerate(nums)))

ans = []

for i in range(n):
    idx,loc = bln[0][0],bln[0][1]
    ans.append(idx+1)
    bln.popleft()
    if loc > 0:
        bln.rotate(-(loc-1))
    else:
        bln.rotate(-loc)

print(*ans)