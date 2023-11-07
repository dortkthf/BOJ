def solution(n, works):
    answer = 0
    lw = len(works)
    s = 0
    works.sort(reverse=True)
    if sum(works) <= n:
        return 0
    else:
        while n:
            if lw == 1:
                return (works[0]-n)**2
            else:
                if s == 0:
                    works[s] -= 1
                    n-=1
                    if works[s] >= works[s+1]:
                        continue
                    else:
                        s+=1
                else:
                    if s == lw-1:
                        works[s] -= 1
                        n-=1
                        if works[s-1] >= works[s]:
                            s-=1
                        else:
                            continue
                    else:
                        if works[s-1] >= works[s] >= works[s+1]:
                            s -= 1
                        else:
                            works[s] -= 1
                            n-=1
                            s+=1
        for w in works:
            answer += w**2
    return answer