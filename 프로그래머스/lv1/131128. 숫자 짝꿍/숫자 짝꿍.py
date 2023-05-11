def solution(X, Y):
    answer = ''
    xlist = list(0 for i in range(10))
    ylist = list(0 for i in range(10))
    for i in X:
        xlist[int(i)] += 1
    for i in Y:
        ylist[int(i)] += 1
    for i in range(9,-1,-1):
        if xlist[i] and ylist[i]:
            answer+=str(i)*min(xlist[i],ylist[i])

    if len(answer) == 0:
        return '-1'
    elif answer[0] == '0':
        return '0'
    return answer