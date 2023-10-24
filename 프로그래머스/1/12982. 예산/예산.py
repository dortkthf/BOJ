def solution(d, budget):
    answer = 0
    sorted_d = sorted(d)
    cnt = 0
    for i in sorted_d:
        cnt += i
        if cnt > budget:
            return answer
        answer+=1
    return answer