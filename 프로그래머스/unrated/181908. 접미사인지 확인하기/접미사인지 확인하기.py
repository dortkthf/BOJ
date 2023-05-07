def solution(my_string, is_suffix):
    res = []
    for i in range(len(my_string)):
        res.append(my_string[i:])
    if is_suffix in res:
        return 1
    else:
        return 0
