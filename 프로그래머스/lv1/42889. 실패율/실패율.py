def solution(N, stages):
    answer = []
    stay = [0 for i in range(N+2)]
    
    for i in stages:
        stay[i] += 1
    
    accumulation = stay[::-1]
    tmp = 0
    
    for i in range(len(accumulation)):
        if accumulation[i] != 0:
            accumulation[i]+=tmp
            tmp=accumulation[i]
    
    accumulation = accumulation[::-1]
    
    for i in range(1,N+1):
        if stay[i] != 0:
            answer.append((stay[i]/accumulation[i],i))
        else:
            answer.append((0,i))
    answer.sort(key = lambda x: (-x[0],x[1]))
    res = [i[1] for i in answer ]
    return res