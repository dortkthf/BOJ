import sys
input = sys.stdin.readline
res = []
t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    cnt = 0
    n = int(input())
    for _ in range(n):
        x,y,r = map(int,input().split())
        if ((x-x1)**2+(y-y1)**2) < r**2 and ((x-x2)**2+(y-y2)**2) < r**2:
            pass
        elif (((x-x1)**2+(y-y1)**2) < r**2 and ((x-x2)**2+(y-y2)**2) > r**2) or (((x-x1)**2+(y-y1)**2) > r**2 and ((x-x2)**2+(y-y2)**2) < r**2):
            cnt+=1
    print(cnt)