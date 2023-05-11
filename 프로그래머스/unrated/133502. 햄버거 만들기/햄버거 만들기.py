def solution(ingredient):
    answer = 0
    cnt = 0
    queue = []
    for i in range(len(ingredient)):
        queue.append(ingredient[i])
        if len(queue) >= 4 and queue[-4:] == [1,2,3,1]:
            queue.pop()
            queue.pop()
            queue.pop()
            queue.pop()
            answer+=1
    return answer