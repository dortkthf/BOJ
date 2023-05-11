def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace('aya','1')
        babbling[i] = babbling[i].replace('ye','2')
        babbling[i] = babbling[i].replace('woo','3')
        babbling[i] = babbling[i].replace('ma','4')
    
    for bab in babbling:
        if bab.isdigit():
            if '11' in bab or '22' in bab or '33' in bab or '44' in bab:
                continue
            else:
                answer+=1
    return answer