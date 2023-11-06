from collections import deque

def solution(n, computers):
    answer = 0
    check = []
    stack = deque([])
    for i in range(n):
        if i not in check:
            check.append(i)
            stack.append(i)
            while stack:
                find = stack.popleft()
                for j in range(n):
                    if computers[find][j] == 1 and j not in check:
                        check.append(j)
                        stack.append(j)
            answer+=1
    return answer