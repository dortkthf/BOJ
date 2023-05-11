import itertools

def solution(number):
    answer = 0
    combs = list(itertools.combinations(number,3))
    for c in combs:
        if sum(c) == 0:
            answer+=1
    return answer