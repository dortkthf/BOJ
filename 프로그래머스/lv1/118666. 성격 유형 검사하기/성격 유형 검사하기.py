def solution(survey, choices):
    answer = ''
    res = {}
    for i in ('R','T','C','F','J','M','A','N'):
        res[i] = 0
    for i in range(len(survey)):
        if choices[i] < 4:
            res[survey[i][0]] += 4-choices[i]
        else:
            res[survey[i][1]] += choices[i]-4
    for i in ([['R','T'],['C','F'],['J','M'],['A','N']]):
        i.sort()
        if res[i[0]] >= res[i[1]]:
            answer+=i[0]
        else:
            answer+=i[1]
    return answer