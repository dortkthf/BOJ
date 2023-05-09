def solution(n, m, section):
    answer = 0
    for i in range(len(section)):
        if i == 0:
            s = section[i] + m-1
            answer+=1            
        elif s<section[i]:
            s = section[i]+ m-1
            answer+=1
    return answer