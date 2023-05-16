def solution(sequence, k):
    answer = []
    cnt = 3000000
    l,r = 0,0
    lensq = len(sequence)
    ss = sequence[0]
    while l<=r and r<lensq:
        if ss == k:
            if cnt > r-l+1:
                cnt = r-l+1
                answer.append(l)
                answer.append(r)
            ss-=sequence[l]
            l+=1
        elif ss > k:
            ss-=sequence[l]
            l+=1
        elif ss < k:
            r+=1
            if r<lensq:
                ss+=sequence[r]
    return answer[-2:]