import sys
read = lambda :sys.stdin.readline()
N, M = map(int, read().split())

ry, rx, rdir = map(int, read().split())
maap = []

for _ in range(N):
    temp = [int(a) for a in read().split()]
    maap.append(temp)


def go2(y, x, dir):
    global maap, visited
    if dir == 0: #북
        adj = [(y, x-1), (y+1, x), (y, x+1), (y-1, x)]
        dirs = [3, 2, 1, 0]
        for (dy, dx), ddir in zip(adj, dirs):
            if 0<=dy<N and 0<=dx<M and not visited[dy][dx] and maap[dy][dx] != 1:
                go(dy, dx, ddir)
                return
        if y+1 < N and maap[y+1][x] != 1:
            go2(y+1, x, dir)
        elif y+1 < N and maap[y+1][x] == 1:
            return
    elif dir == 1:
        adj = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
        dirs = [0,3,2,1]

        for (dy, dx), ddir in zip(adj, dirs):
            if 0 <= dy < N and 0 <= dx < M and not visited[dy][dx] and maap[dy][dx] != 1:
                go(dy, dx, ddir)
                return
        if x -1 >= 0 and maap[y][x-1] != 1:
            go2(y, x-1, dir)
        elif x - 1 >= 0 and maap[y][x-1] == 1:
            return
    elif dir == 2:
        adj = [(y, x+1), (y-1, x), (y, x-1), (y+1, x)]
        dirs = [1, 0, 3, 2]
        for (dy, dx), ddir in zip(adj, dirs):
            if 0 <= dy < N and 0 <= dx < M and not visited[dy][dx] and maap[dy][dx] != 1:
                go(dy, dx, ddir)
                return
        if y - 1 >= 0 and maap[y - 1][x] != 1:
            go2(y - 1, x, dir)
        elif y - 1 >= 0 and maap[y - 1][x] == 1:
            return
    else:
        adj = [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]
        dirs = [2, 1, 0, 3]
        for (dy, dx), ddir in zip(adj, dirs):
            if 0 <= dy < N and 0 <= dx < M and not visited[dy][dx] and maap[dy][dx] != 1:
                go(dy, dx, ddir)
                return
        if x + 1 < M and maap[y][x+1] != 1:
            go2(y, x+1, dir)
        elif x + 1 < M and maap[y][x+1] == 1:
            return


def go(y, x, dir):
    global maap, visited
    visited[y][x] = True
    go2(y, x, dir)


visited = [[False] * M for _ in range(N)]
go(ry, rx, rdir)
cnt = 0
for i in range(N):
    for j in range(M):
       if visited[i][j] == True:
           cnt += 1
print(cnt)