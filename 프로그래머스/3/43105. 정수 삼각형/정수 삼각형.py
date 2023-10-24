def solution(triangle):
    answer = 0
    len_triangle = len(triangle)
    
    find = list(list(0 for i in range(i+1)) for i in range(len_triangle))
    
    for i in range(len_triangle):
        if i == 0:
            find[i][i] = triangle[i][i]
        else:
            for j in range(i+1):
                if j == 0:
                    find[i][j] = triangle[i][j] + find[i-1][j]
                elif j == i:
                    find[i][j] = triangle[i][j] + find[i-1][j-1]
                else:
                    find[i][j] = max(triangle[i][j] + find[i-1][j], triangle[i][j] + find[i-1][j-1])
    answer = max(find[-1])
    return answer