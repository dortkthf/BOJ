import sys
input = sys.stdin.readline

# a 와 b 가 m 으로 나눈 나머지가 동일하면 a-b는 m 의 배수이다

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()

nums2 = []

res = []

for i in range(n-1):
    nums2.append(nums[i+1]-nums[i])

for i in nums2:
    nums3 = [] 
    for j in range(1,int(i**(1/2))+1):
        if i%j == 0:
            nums3.append(j)
            nums3.append(i//j)
    nums3.sort()
    for k in nums3:
        for a in nums:
            if nums.index(a) == 0:
                tmp = a%k
            if a%k != tmp:
                break
        else:
            res.append(k)
res = list(set(res))
res.sort()
res.remove(1)
print(*res, sep=' ')