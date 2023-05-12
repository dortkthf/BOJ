def solution(board, moves):
    answer = 0
    queue = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                queue.append(board[i][m-1])
                board[i][m-1] = 0
                if len(queue) > 1:
                    if queue[-1] == queue[-2]:
                        queue.pop()
                        queue.pop()
                        answer+=2
                break
    return answer