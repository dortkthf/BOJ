import sys
input = sys.stdin.readline

n,k = map(int,input().split())

p = 1000000007

nfac = 1
nkfac = 1
kfac = 1

for i in range(1,n+1):
    nfac*=i
    nfac%=p

for i in range(1,n-k+1):
    nkfac*=i
    nkfac%=p

for i in range(1,k+1):
    kfac*=i
    kfac%=p

p2 = (nkfac*kfac)%p

ans = 1
def find(a,b,c):
    global ans
    
    ans*=a
    ans%=c

    if b==1:
        return
    elif b%2 == 0:
        find(ans,b//2,c)
        return
    elif b%2 != 0:
        k = ans
        find(ans,b//2,c)
        ans*=k
        ans%=c
        return

find(p2,p-2,p)
ans*=nfac
print(ans%p)