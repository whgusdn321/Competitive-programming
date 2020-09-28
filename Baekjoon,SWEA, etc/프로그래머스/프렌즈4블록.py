def down(m, n, board):
    for w in range(n):
        tmp = []
        for h in range(m-1, -1, -1):
            if board[h][w]:
                tmp.append(board[h][w])
        h = m-1
        while tmp:
            board[h][w] = tmp[-1]
            tmp.pop()
            h -= 1
        while h >= 0:
            # print("h is : ", h)
            board[h][w] = 0
            h -= 1


def search(m, n, board):
    ret = []
    for y in range(m-1):
        for x in range(n-1):
            ch = board[y][x]
            if (board[y][x], board[y][x+1], board[y+1][x], board[y+1][x+1]) == \
                    (ch, ch, ch, ch) and ch != 0:
                ret.append((y, x))
    return ret


def solution(m, n, board_):
    ans = 0
    board = []
    for row in board_:
        board.append([ch for ch in row])
    while 1:
        to_remove = search(m, n, board)
        if not to_remove:
            break
        for y, x in to_remove:
            for yy in range(y, y+2):
                for xx in range(x, x+2):
                    if board[yy][xx]:
                        board[yy][xx] = 0
                        ans += 1

        down(m, n, board)
    return ans

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))