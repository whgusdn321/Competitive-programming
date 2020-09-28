def solution(board, moves):
    answer = 0
    H = len(board)
    W = len(board[0])
    knap = []
    stacks = [[] for _ in range(len(board[0]))]
    for j in range(W):
        for i in range(H-1, -1, -1):
            if board[i][j]:
                stacks[j].append(board[i][j])
    for move in moves:
        move -= 1
        if stacks[move]:
            last_elem = stacks[move].pop()
            if knap and knap[-1] == last_elem:
                knap.pop()
                answer += 2
            else:
                knap.append(last_elem)
    return answer