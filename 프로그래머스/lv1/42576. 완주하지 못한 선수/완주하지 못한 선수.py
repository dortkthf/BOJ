def solution(participant, completion):
    answer = ''
    marathon = {}
    
    for i in participant:
        if i in marathon:
            marathon[i][0]+=1
        else:
            marathon[i] = [1,0]
    
    for i in completion:
        marathon[i][1] +=1
    
    for k,v in marathon.items():
        if v[0] != v[1]:
            return k
    
