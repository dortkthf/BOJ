import sys

n = int(input())
liquid = list(map(int,input().split()))
liquid.sort()

def chemical(start,end,cnt):
    l,r = 0,0
    while start < end:
        if liquid[start]+liquid[end] == 0:
            return liquid[start], liquid[end]
        elif liquid[start] + liquid[end] < 0:
            if abs(liquid[start] + liquid[end]) < cnt:
                cnt = abs(liquid[start] + liquid[end])
                l,r = liquid[start], liquid[end]
            start+=1
        elif liquid[start] + liquid[end] > 0:
            if abs(liquid[start]+liquid[end]) < cnt:
                cnt = abs(liquid[start] + liquid[end])
                l,r = liquid[start], liquid[end]
            end-=1
    return l,r

print(*chemical(0,n-1,sys.maxsize))