import sys, bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
res = [a[0]]

for num in a:
    if res[-1] < num:
        res.append(num)
        continue
    index = bisect.bisect_left(res,num)
    res[index] = num

print(len(res))