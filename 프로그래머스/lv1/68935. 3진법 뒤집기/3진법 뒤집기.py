def solution(n):
    answer = []
    cnt = 0
    res = 0
    while True:
        cnt+=1
        if 3**cnt > n:
            cnt-=1
            break
            
    for i in range(cnt,-1,-1):
        answer.append(n//(3**i))
        n = n%(3**i)
    
    for i in range(cnt+1):
        res+=answer[i]*(3**i)
    
    return res