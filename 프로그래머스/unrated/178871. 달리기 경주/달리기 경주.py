def solution(players, callings):
    res = {}
    for i in range(len(players)):
        res[players[i]] = i
    for i in callings:
        n = res[i]
        tmp = players[n-1]
        players[n-1] = i
        players[n] = tmp
        res[i] -= 1
        res[tmp] += 1
    return players
