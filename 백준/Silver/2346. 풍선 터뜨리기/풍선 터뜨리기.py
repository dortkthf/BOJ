from collections import deque

n = int(input())
bln = deque(enumerate(map(int,input().split())))
ans = []

for i in range(n):
    idx,loc = bln.popleft()
    ans.append(idx+1)

    if loc > 0:
        bln.rotate(-(loc-1))
    else:
        bln.rotate(-loc)

print(' '.join(map(str,ans)))