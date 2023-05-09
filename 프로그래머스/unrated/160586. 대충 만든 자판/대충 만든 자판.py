def solution(keymap, targets):
    answer = []
    for tar in targets:
        tmp1 = []
        for t in tar:
            tmp = -1
            for key in keymap:
                if key.find(t) == 0:
                    tmp = 0
                    break
                elif key.find(t) >= 0 and tmp < 0:
                    tmp = key.find(t)
                elif key.find(t) >= 0 and tmp >= 0 and key.find(t) < tmp:
                    tmp = key.find(t)
            if tmp == -1:
                tmp1.append(-1)
                break
            else:
                tmp1.append(tmp+1)
        stmp = sum(tmp1)
        if -1 in tmp1:
            answer.append(-1)
        else:
            answer.append(stmp)
    return answer