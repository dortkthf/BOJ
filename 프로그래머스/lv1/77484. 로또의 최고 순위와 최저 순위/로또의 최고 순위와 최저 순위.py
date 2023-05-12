def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    tmp = 0
    for i in lottos:
        if i in win_nums:
            win_nums.remove(i)
            tmp+=1
    win = tmp+zero
    lose = tmp
    if win>=2:
        answer.append(7-win)
    else:
        answer.append(6)
    if lose>=2:
        answer.append(7-lose)
    else:
        answer.append(6)
    return answer