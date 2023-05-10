def solution(number, limit, power):
    answer = 0
    res = []
    for i in range(1,number+1):
        tmp = 0
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                if i//j == j:
                    tmp+=1
                else:
                    tmp+=2
        if tmp > limit:
            tmp = power
        res.append(tmp)
    return sum(res)    
