import sys
H, W = map(int, sys.stdin.readline().split())
r_y, r_x, r_dir = map(int, sys.stdin.readline().split())
maap = []
visited = []
for _ in range(H):
    temp = [int(a) for a in sys.stdin.readline().split()]
    maap.append(temp)
    temp2 = [False]*W
    visited.append(temp2)


def go(y, x, direc, maap, visited):
    global cnt
    cnt += 1
    visited[y][x] = True

    while(True):
        if direc == 0:
            adjacent = [(y, x-1), (y+1, x), (y, x+1), (y-1, x)]
            directions = [3, 2, 1, 0]

            for (n_y, n_x), dir in zip(adjacent, directions):
                if 0<=n_y<H and 0<=n_x<W:
                    if maap[n_y][n_x] == 0 and not visited[n_y][n_x]:
                        go(n_y, n_x, dir, maap, visited)
                        return
            if (0<=y+1<H) and (0<=x<W) and maap[y+1][x] == 0:
                y = y+1
                x = x
                continue
            else:
                return

        elif direc == 1:
            adjacent = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
            directions = [0, 3, 2, 1]

            for (n_y, n_x), dir in zip(adjacent, directions):
                if 0 <= n_y < H and 0 <= n_x < W:
                    if maap[n_y][n_x] == 0 and not visited[n_y][n_x]:
                        go(n_y, n_x, dir, maap, visited)
                        return
            if (0 <= y < H) and (0 <= x-1< W) and maap[y][x-1] == 0:
                y = y
                x = x-1
                continue
            else:
                return

        elif direc == 3:
            adjacent = [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]
            directions = [2, 1, 0, 3]

            for (n_y, n_x), dir in zip(adjacent, directions):
                if 0 <= n_y < H and 0 <= n_x < W:
                    if maap[n_y][n_x] == 0 and not visited[n_y][n_x]:
                        go(n_y, n_x, dir, maap, visited)
                        return
            if (0 <= y < H) and (0 <= x+1 < W) and maap[y][x+1] == 0:
                y = y
                x = x+1
                continue
            else:
                return

        elif direc == 2:
            adjacent = [(y, x+1), (y-1, x), (y, x-1), (y+1, x)]
            directions = [1, 0, 3, 2]

            for (n_y, n_x), dir in zip(adjacent, directions):
                if 0 <= n_y < H and 0 <= n_x < W:
                    if maap[n_y][n_x] == 0 and not visited[n_y][n_x]:
                        go(n_y, n_x, dir, maap, visited)
                        return
            if (0 <= y-1 < H) and (0 <= x < W) and maap[y-1][x] == 0:
                y = y-1
                x = x
                continue
            else:
                break


cnt = 0
go(r_y, r_x, r_dir, maap, visited)
print(cnt)