import sys
input = sys.stdin.readline

n,s = map(int,input().split())
numbers = list(map(int,input().split()))

if s in numbers:
    print(1)
    exit(0)

def find(start,end,res,snum):
    while start < end and end < n:
        if snum >= s:
            if res > end-start+1:
                res = end-start+1
            snum-=numbers[start]
            start+=1
        elif snum < s:
            end+=1
            if end < n:
                snum+=numbers[end]
    return res

if find(0,1,100001,numbers[0]+numbers[1]) == 100001:
    print(0)
else:
    print(find(0,1,100001,numbers[0]+numbers[1]))