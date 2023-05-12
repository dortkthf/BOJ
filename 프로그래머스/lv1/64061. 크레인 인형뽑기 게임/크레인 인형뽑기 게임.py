def solution(board, moves):
    answer = 0
    queue = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if queue:
                    if queue[-1] == board[i][m-1]:
                        queue.pop()
                        answer+=2
                        board[i][m-1] = 0
                        break
                    else:
                        queue.append(board[i][m-1])
                        board[i][m-1] = 0
                        break
                else:
                    queue.append(board[i][m-1])
                    board[i][m-1] = 0
                    break
    return answer