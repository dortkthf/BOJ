import sys
input = sys.stdin.readline

n = int(input())
mtx = [[0,0]] + [list(map(int,input().split())) for i in range(n)]
dp = [list([0,0,0] for i in range(n+1)) for i in range(n+1)]
maxs = sys.maxsize

for i in range(1,n):
    dp[i][i] = [mtx[i][0],mtx[i][1],0]
    dp[i][i+1] = [mtx[i][0],mtx[i+1][1],mtx[i][0]*mtx[i][1]*mtx[i+1][1]]
dp[n][n] = [mtx[n][0],mtx[n][1],0]
for i in range(n-1,0,-1):
    for j in range(i,n+1):
        if j>i and dp[i][j] == [0,0,0]:
            dp[i][j] = [0, 0, maxs]
            for k in range(i,j):
                dp[i][j] = min(dp[i][j],[dp[i][k][0],dp[k+1][j][1],dp[i][k][2]+dp[k+1][j][2]+dp[i][k][0]*dp[i][k][1]*dp[k+1][j][1]],key=lambda x: x[2])

print(dp[1][n][2])