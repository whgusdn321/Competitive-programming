
def dfs(y, x, board, dp, n, mode):
    dp[y][x] = n
    h = len(board)
    w = len(board[0])
    if y == h and x == w:
        return

    right = [(y, x+1), (y, x-1)]
    up = [(y+1, x), (y-1, x)]
    if mode == 'down':
        for ny, nx in right:
            if 0<=ny<h and 0<=nx<w and dp[ny][nx] >= n + 500 and board[ny][nx] == 0:
                dfs(ny, nx, board, dp, n+600, 'right')
        for ny, nx in up:
            if 0<=ny<h and 0<=nx<w and dp[ny][nx] >= n + 100 and board[ny][nx] == 0:
                dfs(ny, nx, board, dp, n+100, 'down')
    else:
        for ny, nx in right:
            if 0<=ny<h and 0<=nx<w and dp[ny][nx] >= n + 100 and board[ny][nx] == 0:
                dfs(ny, nx, board, dp, n+100, 'right')
        for ny, nx in up:
            if 0<=ny<h and 0<=nx<w and dp[ny][nx] >= n + 500 and board[ny][nx] == 0:
                dfs(ny, nx, board, dp, n+600, 'down')


def solution(board):
    h = len(board)
    w = len(board[0])
    dp = [[9999999]*w for _ in range(h)]
    dfs(0, 0, board, dp, 0, 'down')
    dfs(0, 0, board, dp, 0, 'right')
    for row in dp:
        print(row)
    return dp[h-1][w-1]

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))