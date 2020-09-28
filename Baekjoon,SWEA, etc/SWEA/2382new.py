"""
오답노트 참고.

"""
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    visited = [[False]*N for _ in range(N)]
    points = [[0]*N for _ in range(N)]
    dirs = [[-1] * N for _ in range(N)]
    germs = []
    for _ in range(K):
        h, w, n, dir = map(int, input().split())
        points[h][w] = n
        dirs[h][w] = dir
        visited[h][w] = True
        germs.append([h, w])

    cur = germs
    for _ in range(M):
        cur.sort(key = lambda x:points[x[0]][x[1]])
        next = []
        for y, x in cur:
            if dirs[y][x] == 1:
                visited[y][x] = False
                temp = points[y][x]
                dir2 = dirs[y][x]
                points[y][x] = 0
                dirs[y][x] = -1
                y -= 1
                next.append([y, x, temp, dir2])
            elif dirs[y][x] == 4:
                visited[y][x] = False
                temp = points[y][x]
                dir2 = dirs[y][x]
                points[y][x] = 0
                dirs[y][x] = -1
                x += 1
                next.append([y, x, temp, dir2])
            elif dirs[y][x] == 3:
                visited[y][x] = False
                temp = points[y][x]
                dir2 = dirs[y][x]
                points[y][x] = 0
                dirs[y][x] = -1
                x -= 1
                next.append([y, x, temp, dir2])
            else:
                visited[y][x] = False
                temp = points[y][x]
                dir2 = dirs[y][x]
                points[y][x] = 0
                dirs[y][x] = -1
                y += 1
                next.append([y, x, temp, dir2])

        real_next = []
        for i in range(len(cur)):
            cy, cx = cur[i]
            ny, nx, point, dir = next[i]

            if visited[ny][nx]:
                points[ny][nx] += point
                dirs[ny][nx] = dir
            else:
                if ny == 0:
                    points[ny][nx] = point // 2
                    dirs[ny][nx] = 2
                    visited[ny][nx] = True
                elif ny == N-1:
                    points[ny][nx] = point // 2
                    dirs[ny][nx] = 1
                    visited[ny][nx] = True
                elif nx == 0:
                    points[ny][nx] = point // 2
                    dirs[ny][nx] = 4
                    visited[ny][nx] = True
                elif nx == N-1:
                    points[ny][nx] = point // 2
                    dirs[ny][nx] = 3
                    visited[ny][nx] = True
                else:
                    points[ny][nx] = point
                    dirs[ny][nx] = dir
                    visited[ny][nx] = True
                real_next.append([ny, nx])
        cur = real_next

    res = 0
    for i in range(N):
        for j in range(N):
            res += points[i][j]
    print('#{} {}'.format(tc, res))


