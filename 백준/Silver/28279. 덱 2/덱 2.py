from collections import deque
import sys

input = sys.stdin.readline

d = deque()

n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    std = a[0] 
    if std == 1:
        d.appendleft(a[1])
    elif std == 2:
        d.append(a[1])
    elif std == 5:
        print(len(d))
    else:
        if d:
            if std == 3:
                print(d.popleft())
            elif std == 4:
                print(d.pop())
            elif std == 6:
                print(0)
            elif std == 7:
                print(d[0])
            elif std == 8:
                print(d[-1])
        else:
            if std == 6:
                print(1)
            else:
                print(-1)