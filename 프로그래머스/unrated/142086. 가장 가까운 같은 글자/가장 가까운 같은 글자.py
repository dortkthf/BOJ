def solution(s):
    answer = []
    lens = len(s)
    for i in range(lens):
        tmp = -1
        for j in range(i):
            if s[j] == s[i]:
                tmp = i-j
        answer.append(tmp)
    return answer