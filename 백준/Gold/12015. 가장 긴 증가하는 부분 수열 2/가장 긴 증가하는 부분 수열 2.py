import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dp = [0,a[0]] + list(0 for i in range(n-1))
current = 1

def bs(left,right,value):
    mid = (left+right)//2

    if value > dp[right]:
        return -1
    if right-left == 1:
        if dp[left] < value and value <= dp[right]:
            return right
    if value > dp[mid]:
        return bs(mid,right,value)
    if value <= dp[mid]:
        return bs(left,mid,value)

for i in range(1,n):
    index = bs(0,current,a[i])
    if index == -1:
        current+=1
        dp[current] = a[i]
    else:
        dp[index] = a[i]

print(current)