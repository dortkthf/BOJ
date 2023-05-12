def solution(n, lost, reserve):
    answer = 0
    nlost = list(set(lost[:])-set(reserve[:]))
    nreserve = set(reserve[:])-set(lost[:])
    lost = nlost[:]
    lost.sort()
    for i in lost:
        if i-1 in nreserve:
            nreserve.remove(i-1)
            nlost.remove(i)
        elif i+1 in nreserve:
            nreserve.remove(i+1)
            nlost.remove(i)
    return n-len(nlost)