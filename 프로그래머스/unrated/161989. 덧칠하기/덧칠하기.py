def solution(n, m, section):
    answer = 0
    for i in range(len(section)):
        if i == 0:
            s = section[i] + m-1
            answer+=1            
        elif s>=section[i]:
            continue
        else:
            s = section[i]+ m-1
            answer+=1
    return answer