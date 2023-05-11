def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    r = len(score)//m
    for i in range(r):
        answer+=score[m-1+i*m]*m
    return answer