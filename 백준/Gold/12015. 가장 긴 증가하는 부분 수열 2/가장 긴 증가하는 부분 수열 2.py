import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dp = list(0 for i in range(n+1))
current = 0

def bs(left,right,value):
    mid = (left+right)//2

    if value > dp[right]:
        return -1
    if right-left == 1:
        if dp[left] < value and value <= dp[right]:
            return right
    if value > dp[mid] and value <= dp[right]:
        return bs(mid,right,value)
    if value > dp[left] and value <= dp[mid]:
        return bs(left,mid,value)

for i in range(n):
    if i == 0:
        dp[i+1] = a[i]
        current+=1
        continue
    index = bs(0,current,a[i])
    if index == -1:
        current+=1
        dp[current] = a[i]
    else:
        dp[index] = a[i]

print(current)