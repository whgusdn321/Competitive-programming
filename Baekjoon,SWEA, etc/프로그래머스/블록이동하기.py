from collections import deque, defaultdict


def solution(board):
    n = len(board)
    visited = defaultdict(bool)
    dq = deque([])
    dq.append((0, 0, 'garo', 0))
    visited[(0, 0, 'garo')] = True
    ans = int(10e9)
    while dq:
        y, x, mode, time = dq.popleft()
        if mode == 'garo' and y == n - 1 and x == n - 2:
            ans = min(ans, time)
        if mode == 'sero' and y == n - 1 and x == n - 1:
            ans = min(ans, time)

        if mode == 'garo':
            if x - 1 >= 0 and board[y][x - 1] == 0 and not visited[(y, x - 1, 'garo')]:
                dq.append((y, x - 1, 'garo', time + 1))
                visited[(y, x - 1, 'garo', time + 1)] = True
            if x + 2 < n and board[y][x + 2] == 0 and not visited[(y, x + 1, 'garo')]:
                dq.append((y, x + 1, 'garo', time + 1))
                visited[(y, x + 1, 'garo')] = True
            if y + 1 < n and board[y + 1][x] == 0 and board[y + 1][x + 1] == 0:
                if not visited[(y + 1, x, 'garo')]:
                    dq.append((y + 1, x, 'garo', time + 1))
                    visited[(y + 1, x, 'garo')] = True
                if not visited[(y + 1, x, 'sero')]:
                    dq.append((y + 1, x, 'sero', time + 1))
                    visited[(y + 1, x, 'sero')] = True
                if not visited[(y + 1, x + 1, 'sero')]:
                    dq.append((y + 1, x + 1, 'sero', time + 1))
                    visited[(y + 1, x + 1, 'sero')] = True
            if y - 1 >= 0 and board[y - 1][x] == 0 and board[y - 1][x + 1] == 0:
                if not visited[(y - 1, x, 'garo')]:
                    dq.append((y - 1, x, 'garo', time + 1))
                    visited[(y - 1, x, 'garo')] = True
                if not visited[(y, x, 'sero')]:
                    dq.append((y, x, 'sero', time + 1))
                    visited[(y, x, 'sero')] = True
                if not visited[(y, x + 1, 'sero')]:
                    dq.append((y, x + 1, 'sero', time + 1))
                    visited[(y, x + 1, 'sero')] = True
        if mode == 'sero':
            if y + 1 < n and board[y + 1][x] == 0 and not visited[(y + 1, x, 'sero')]:
                dq.append((y + 1, x, 'sero', time + 1))
                visited[(y + 1, x, 'sero')] = True
            if y - 2 >= 0 and board[y - 2][x] == 0 and not visited[(y - 1, x, 'sero')]:
                dq.append((y - 1, x, 'sero', time + 1))
                visited[(y - 1, x, 'sero')] = True
            if x + 1 < n and board[y][x + 1] == 0 and board[y - 1][x + 1] == 0:
                if not visited[(y, x + 1, 'sero')]:
                    dq.append((y, x + 1, 'sero', time + 1))
                    visited[(y, x + 1, 'sero')] = True
                if not visited[(y, x, 'garo')]:
                    dq.append((y, x, 'garo', time + 1))
                    visited[(y, x, 'garo')] = True
                if not visited[(y - 1, x, 'garo')]:
                    dq.append((y - 1, x, 'garo', time + 1))
                    visited[(y - 1, x, 'garo')] = True
            if x - 1 >= 0 and board[y][x - 1] == 0 and board[y - 1][x - 1] == 0:
                if not visited[(y, x - 1, 'sero')]:
                    dq.append((y, x - 1, 'sero', time + 1))
                    visited[(y, x - 1, 'sero')] = True
                if not visited[(y, x - 1, 'garo')]:
                    dq.append((y, x - 1, 'garo', time + 1))
                    visited[(y, x - 1, 'garo')] = True
                if not visited[(y - 1, x - 1, 'garo')]:
                    dq.append((y - 1, x - 1, 'garo', time + 1))
                    visited[(y - 1, x - 1, 'garo')] = True
    return ans
