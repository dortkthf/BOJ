from itertools import combinations
import bisect

n,c = map(int,input().split())
nums = list(map(int,input().split()))

left_nums = nums[:n//2]
right_nums = nums[n//2:]

def sum_list(nums_list):
    nums_sum_list = []
    for i in range(len(nums_list)+1):
        for com in combinations(nums_list,i):
            nums_sum_list.append(sum(com))
    return nums_sum_list

def calculation(left,right,c):
    left.sort()
    ans = 0
    for i in right:
        max_y = c-i
        ans += bisect.bisect_right(left,max_y)
    return ans

print(calculation(sum_list(left_nums),sum_list(right_nums),c))