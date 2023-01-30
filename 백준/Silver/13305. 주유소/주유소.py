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

cheap_len = len(cheap)

dp = [0 for i in range(n-1)]

for i in range(n-1):
    if i == 0:
        dp[i] = way[i]
        continue
    dp[i] = way[i] + dp[i-1]

if cheap_len == 0:
    print(dp[-1]*oil[0])
elif cheap_len == 1:
    print(dp[cheap[0]-1]*oil[0]+(dp[-1]-dp[cheap[0]-1])*oil[cheap[0]])
else:
    s = 0
    ans = 0
    for i in range(cheap_len):
        if i == 0:
            ans+=dp[cheap[i]-1]*oil[0]
            s = cheap[i]
        elif i == cheap_len-1:
            ans+=((dp[cheap[i]-1]-dp[s-1])*oil[s])+((dp[-1]-dp[cheap[i]-1])*oil[cheap[i]])
        else:
            ans+=(dp[cheap[i]-1]-dp[s-1])*oil[s]
    print(ans)