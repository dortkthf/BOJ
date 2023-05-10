def solution(k, score):
    answer = []
    tmp = []
    for i in range(len(score)):
        tmp.append(score[i])
        tmp.sort(reverse=True)
        if i < k:
            answer.append(tmp[-1])
        else:
            answer.append(tmp[k-1])        
    return answer