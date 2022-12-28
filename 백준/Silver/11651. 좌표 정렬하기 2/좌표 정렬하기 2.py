from sys import stdin
input = stdin.readline

n = int(input())
ls = []
for _ in range(n):
    x,y = map(int,input().split())
    ls.append([y,x])
ls.sort()
for x,y in ls:
    print(y,x)