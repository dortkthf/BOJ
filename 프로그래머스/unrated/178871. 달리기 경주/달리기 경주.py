def solution(players, callings):
    res = {}
    for i in range(len(players)):
        res[players[i]] = i
    for i in callings:
        n = res[i]
        tmp = players[n-1]
        res[i] = n-1
        res[tmp] = n
        players[n-1] = i
        players[n] = tmp
    
    return players