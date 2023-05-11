def solution(babbling):
    answer = 0
    for b in babbling:
        for j in ["aya", "ye", "woo", "ma"]:
            if j*2 in b:
                break
            else:
                b = b.replace(j,' ')
        if len(b.replace(' ','')) == 0:
            answer+=1
    return answer