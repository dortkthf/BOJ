def solution(answers):
    answer = []
    one = [1,2,3,4,5]*2000
    two = [2,1,2,3,2,4,2,5]*1250
    three = [3,3,1,1,2,2,4,4,5,5]*1000
    
    scores = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == one[i]:
            scores[0]+=1
        if answers[i] == two[i]:
            scores[1]+=1
        if answers[i] == three[i]:
            scores[2]+=1

    for i,v in enumerate(scores):
        if v == max(scores):
            answer.append(i+1)
    return answer