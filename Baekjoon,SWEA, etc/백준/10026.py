import sys
sys.setrecursionlimit(10000000)
read = lambda: sys.stdin.readline().rstrip()
N = int(read())
maap = []
visited = []
for _ in range(N):
    maap.append(read())
    visited.append([False]*N)


def go1(y, x):
    global maap, visited
    color = maap[y][x]
    visited[y][x] = True

    adjacent = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adjacent:
        if 0<=dy<N and 0<=dx<N:
            if not visited[dy][dx] and maap[dy][dx] == color:
                go1(dy, dx)


def go2(y, x):
    global maap, visited
    color = maap[y][x]
    visited[y][x] = True

    if color == 'G' or color == 'R':
        adjacent = [(y, x - 1), (y - 1, x), (y, x + 1), (y + 1, x)]
        for dy, dx in adjacent:
            if 0 <= dy < N and 0 <= dx < N:
                if not visited[dy][dx] and (maap[dy][dx] == 'R' or maap[dy][dx] == 'G'):
                    go2(dy, dx)
    else:
        adjacent = [(y, x - 1), (y - 1, x), (y, x + 1), (y + 1, x)]
        for dy, dx in adjacent:
            if 0 <= dy < N and 0 <= dx < N:
                if not visited[dy][dx] and maap[dy][dx] == color:
                    go2(dy, dx)


cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            go1(i, j)
            cnt1 += 1

visited = [[False]*N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            go2(i, j)
            cnt2 += 1

print('{} {}'.format(cnt1, cnt2))