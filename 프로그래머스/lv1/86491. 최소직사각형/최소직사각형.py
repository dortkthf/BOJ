def solution(sizes):
    answer = 0
    left = []
    right = []
    for s in sizes:
        left.append(max(s))
        right.append(min(s))
    return max(left)*max(right)