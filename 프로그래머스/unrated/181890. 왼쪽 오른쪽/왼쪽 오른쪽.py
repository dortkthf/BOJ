def solution(str_list):
    answer = []
    l = -1
    r = -1
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            l = i
            break
        elif str_list[i] == 'r':
            r = i
            break
    if l != -1 and l != 0:
        return [str_list[i] for i in range(l)]
    elif r != -1 and r != len(str_list)-1:
        return [str_list[i] for i in range(r+1,len(str_list))]
    return answer