def solution(arr):
    answer = []
    s = -1
    e = -1
    for i in range(len(arr)):
        if arr[i] == 2 and s == -1:
            s = i
        elif arr[i] == 2 and s != -1:
            e = i
    if s == -1:
        return [-1]
    else:
        if e == -1:
            return [arr[s]]
        else:
            return [arr[i] for i in range(s,e+1)]
