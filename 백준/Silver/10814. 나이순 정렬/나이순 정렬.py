import sys
input = sys.stdin.readline

n = int(input())
ls = []
cnt=0
for _ in range(n):
    age, name = input().split()
    ls.append([int(age),cnt,name])
    cnt+=1
ls.sort()
for l,s,i in ls:
    print(l,i)