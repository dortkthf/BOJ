import sys
input = sys.stdin.readline

n,s = map(int,input().split())
numbers = list(map(int,input().split()))
numbers+=[0]

def find(start,end,res,snum):
    while start <= end and end < n:
        if snum >= s:
            if res > end-start+1:
                res = end-start+1
            snum-=numbers[start]
            start+=1
        elif snum < s:
            end+=1
            snum+=numbers[end]
    if res == 100001:
        res = 0
    return res

print(find(0,0,100001,numbers[0]))