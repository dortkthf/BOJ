import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    word = input().rstrip()
    if word not in ls:
        ls.append(word)
ls.sort()
ls.sort(key=len)
for word in ls:
    print(word)