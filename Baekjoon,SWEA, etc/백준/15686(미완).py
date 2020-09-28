import sys
read = lambda:sys.stdin.readline().rstrip()

N, M = map(int, read().split())
maap = []

for _ in range(N):
    maap.append([int(a) for a in read().split()])

ones = []
for i in range(N):
    for j in range(N):
        if maap[i][j] == 1:
            ones.append((i, j))


def go(y, x, limit, c):
    global visited, maap
    visited[y][x] = True
    c += 1
    if c > limit:
        return -1
    elif maap[y][x] == 2:
        return c
    else:
        adj = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
        for dy, dx in adj:
            if 0<=dy<N and 0<=dx<N and not visited[dy][dx]:
                f = go(dy, dx, limit, c)
        return f