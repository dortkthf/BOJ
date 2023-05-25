from itertools import combinations
import bisect

n,c = map(int,input().split())
nums = list(map(int,input().split()))

left_nums = nums[:n//2]
right_nums = nums[n//2:]

def make_nums(nums_list):
    sum_nums_list = []
    for i in range(len(nums_list)+1):
        for com in combinations(nums_list,i):
            sum_nums_list.append(sum(com))
    return sum_nums_list

def cal(left_nums,right_nums,c):
    left_nums.sort()
    ans = 0
    for i in right_nums:
        ans+=bisect.bisect_right(left_nums,c-i)
    return ans

print(cal(make_nums(left_nums),make_nums(right_nums),c))