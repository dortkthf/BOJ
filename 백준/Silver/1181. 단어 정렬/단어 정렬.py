import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    word = input().rstrip()
    cnt = len(word)
    if [cnt,word] not in ls:
        ls.append([cnt,word])
ls.sort()
for cnt, word in ls:
    print(word)