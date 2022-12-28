import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    word = input().rstrip()
    ls.append(word)
ls = list(set(ls))
ls.sort()
ls.sort(key=len)
for word in ls:
    print(word)