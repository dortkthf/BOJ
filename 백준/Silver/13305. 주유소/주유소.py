import sys
input = sys.stdin.readline

n = int(input())
way = list(map(int,input().split()))
oil = list(map(int,input().split()))

cheap = []

for i in range(len(oil)):
    if i == 0:
        oil_fst = oil[i]
    elif oil_fst > oil[i] and i != len(oil)-1:
        oil_fst = oil[i]
        cheap.append(i)

if len(cheap) == 0:
    print(sum(way)*oil[0])
else:
    ans = 0
    s = 0
    for i in range(n-1):
        if i in cheap:
            s = i
            ans+=way[i]*oil[s]
            continue
        ans+=way[i]*oil[s]
    print(ans)