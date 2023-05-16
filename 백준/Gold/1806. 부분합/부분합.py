import sys
input = sys.stdin.readline

n,s = map(int,input().split())
numbers = list(map(int,input().split()))
sumnums = [0]
for i in range(n):
    if i == 0:
        sumnums.append(numbers[0])
        continue
    sumnums.append(sumnums[i]+numbers[i])
sumnums.append(0)

if s in numbers:
    print(1)
    exit(0)

def find(start,end,res):
    while start < end and end<=n:
        sumnum = sumnums[end]-sumnums[start-1]
        if sumnum >= s:
            if res > end-start+1:
                res = end-start+1
            start+=1
        elif sumnum < s:
            end+=1
    return res

if find(1,2,100001) == 100001:
    print(0)
else:
    print(find(1,2,100001))