def solution(wallpaper):
    y,x = [],[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                y.append(i)
                x.append(j)
    answer = [min(y),min(x),max(y)+1,max(x)+1]
    return answer