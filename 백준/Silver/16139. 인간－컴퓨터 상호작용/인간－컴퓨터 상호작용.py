import sys
input = sys.stdin.readline

words = input()
wordscnt = len(words)

q = int(input())

dic = {}

for i in 'abcdefghijklmnopqrstuvwxyz':
    dic[i] = [0 for i in range(wordscnt)]

for i in range(wordscnt):
    if i == 0:
        dic[words[i]][i] = 1
        continue
    for j in dic:
        if j == words[i]:
            dic[j][i] = dic[j][i-1]+1
            continue
        dic[j][i] = dic[j][i-1]

for _ in range(q):
    a,i,r = input().split()
    if int(i) == 0:
        print(dic[a][int(r)])
        continue
    print(dic[a][int(r)]-dic[a][int(i)-1])