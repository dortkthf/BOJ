def solution(name, yearning, photo):
    answer = []
    find = {name[i]:yearning[i] for i in range(len(name))}
    for p in photo:
        score = 0
        for i in p:
            if i in find:
                score+=find[i]
        answer.append(score)
    return answer