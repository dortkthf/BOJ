import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int,input().split()))
ls2 = sorted(list(set(ls)))
ls3 = {ls2[i]: i for i in range(len(ls2))}
for i in ls:
    print(ls3[i],end=' ')
