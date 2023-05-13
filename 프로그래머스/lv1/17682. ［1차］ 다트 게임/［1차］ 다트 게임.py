def solution(dartResult):
    answer = []
    score = ''
    scoredic = {'S':1,'D':2,'T':3}
    
    for dart in dartResult:
        if dart.isdigit():
            score+=dart
        else:
            if dart in scoredic:
                score = int(score)**scoredic[dart]
                answer.append(score)
            elif dart == '*':
                if len(answer) > 1:
                    answer[-1]*=2
                    answer[-2]*=2
                else:
                    answer[-1]*=2
            elif dart == '#':
                answer[-1]*=-1
            score = ''
    return sum(answer)