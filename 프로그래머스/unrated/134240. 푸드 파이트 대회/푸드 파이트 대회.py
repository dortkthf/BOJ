def solution(food):
    answer = ''
    for i in range(1,len(food)):
        c = food[i]//2
        if c != 0:
            answer+=(str(i)*c)
    answer = answer+'0'+answer[::-1]
    return answer