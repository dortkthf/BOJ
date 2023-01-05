import sys, math
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()
gcd = nums[1] - nums[0]
res = []
for i in range(n-1):
    gcd = math.gcd(gcd,nums[i+1]-nums[i])
for i in range(1,int(math.sqrt(gcd))+1):
    if gcd%i == 0:
        res.append(i)
        res.append(gcd//i)
res = list(set(res))
res.sort()
res.remove(1)
print(*res, sep=' ')