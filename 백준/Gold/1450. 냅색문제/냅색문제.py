from itertools import combinations
import bisect

n,c = map(int,input().split())
nums = list(map(int,input().split()))

left_nums = nums[:n//2]
right_nums = nums[n//2:]

def make_nums_sum(nums):
    nums_sum = []
    for i in range(len(nums)+1):
        for com in combinations(nums,i):
            nums_sum.append(sum(com))
    return nums_sum

def find_answer(left,right,c):
    ans = 0
    left.sort()
    for i in right:
        maxvalue = c-i
        ans+=bisect.bisect_right(left,maxvalue)
    return ans

print(find_answer(make_nums_sum(left_nums),make_nums_sum(right_nums),c))