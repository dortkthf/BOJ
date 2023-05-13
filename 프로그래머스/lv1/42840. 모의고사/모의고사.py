def solution(answers):
    answer = []
    one = [1,2,3,4,5]*2000
    two = [2,1,2,3,2,4,2,5]*1250
    three = [3,3,1,1,2,2,4,4,5,5]*1000
    
    ones,twos,threes = 0,0,0
    for i in range(len(answers)):
        if answers[i] == one[i]:
            ones+=1
        if answers[i] == two[i]:
            twos+=1
        if answers[i] == three[i]:
            threes+=1
    answer.append((ones,1))
    answer.append((twos,2))
    answer.append((threes,3))

    cnt = max(ones,twos,threes)
    res = []
    for i in answer:
        if i[0] == cnt:
            res.append(i[1])
    res.sort()
    return res