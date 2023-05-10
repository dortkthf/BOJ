def solution(s):
    answer = 0
    fc,sc = 0,0
    fst = s[0]
    for i in range(len(s)):
        if s[i] == fst:
            fc+=1
        elif s[i] != fst:
            sc+=1
        if fc == sc:
            if i == len(s)-1:
                answer+=1
                break
            fst = s[i+1]
            answer += 1
    else:
        if fc != sc:
            answer+=1
    return answer