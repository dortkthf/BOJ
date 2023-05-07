def solution(my_string, m, c):
    res = []
    answer = ''
    for i in range(len(my_string)//m):
        res.append(my_string[m*i:m*i+m])
    for i in res:
        answer+=i[c-1]
    return answer