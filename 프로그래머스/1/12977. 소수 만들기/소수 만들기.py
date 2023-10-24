from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        sumi = sum(i)
        for j in range(2,int(sumi**(1/2))+1):
            if sumi%j == 0 and sumi != j:
                break
        else:
            answer+=1
    return answer