def solution(dartResult):
    answer = []
    score = ''
    for dart in dartResult:
        if dart.isdigit():
            score+=dart
        else:
            if dart == 'S':
                score = int(score)**1
                answer.append(score)
            elif dart == 'D':
                score = int(score)**2
                answer.append(score)
            elif dart == 'T':
                score = int(score)**3
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