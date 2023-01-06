import math

n = int(input())
ring = list(map(int,input().split()))
for i in range(1,n):
    gcd = math.gcd(ring[0],ring[i])
    print(ring[0]//gcd,ring[i]//gcd,sep='/')