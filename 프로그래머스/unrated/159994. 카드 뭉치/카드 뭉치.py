def solution(cards1, cards2, goal):
    answer = 'Yes'
    c1 = 0
    c2 = 0
    for g in goal:
        if c1<len(cards1) and cards1[c1] == g:
            c1+=1
        elif c2<len(cards2) and cards2[c2] == g:
            c2+=1
        else:
            answer = 'No'
            break
    return answer