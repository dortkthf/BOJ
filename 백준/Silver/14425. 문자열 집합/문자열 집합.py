import sys
input = sys.stdin.readline

n,m = map(int,input().split())
S = set(input().rstrip() for i in range(n))
N = list(input().rstrip() for i in range(m))
cnt = 0
for i in N:
    if i in S:
        cnt+=1
print(cnt)