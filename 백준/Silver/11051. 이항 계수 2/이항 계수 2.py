n,k = map(int,input().split())

nn = 1
kk = 1
nk = 1
for i in range(2,n+1):
    nn*=i
for i in range(2,k+1):
    kk*=i
for i in range(2,n-k+1):
    nk*=i

ans = nn//kk//nk

print(round(ans%10007))
