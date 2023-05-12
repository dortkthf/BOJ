from itertools import combinations

def solution(numbers):
    combnt = combinations(numbers,2)
    answer = [sum(c) for c in combnt]
    answer = list(set(answer))
    answer.sort()
    return answer