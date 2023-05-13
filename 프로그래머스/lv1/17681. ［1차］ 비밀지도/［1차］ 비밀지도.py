def solution(n, arr1, arr2):
    fst = []
    scd = []
    answer = []
    for arr in (arr1,arr2):
        for j in arr:
            tmp = []
            for i in range(n-1,-1,-1):
                tmp.append(j//(2**i))
                j = j%(2**i)
            if arr == arr1:
                fst.append(tmp)
            else:
                scd.append(tmp)
    
    for i in range(n):
        tmp = ''
        for j in range(n):
            if fst[i][j] == 1 or scd[i][j] == 1:
                tmp+='#'
            elif fst[i][j] == 0 and scd[i][j] == 0:
                tmp+=' '
        answer.append(tmp)
    return answer