def simulate(maap):
    global N, results
    # print('maap : ')
    # for i in range(N):
    #     print(maap[i])
    dir = 'E'
    sy, sx = 0, 0
    boool = True
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    while 0<=sy<N and 0<=sx<N and not visited[sy][sx] and maap[sy][sx] != 0:
        visited[sy][sx] = True
        k = maap[sy][sx]
        if k == 1:
            if dir == 'E':
                sx += 1
                dir = 'E'
            else:
                sx -= 1
                dir = 'W'
            cnt += 1
            continue
        elif k == 2:
            if dir == 'N':
                sy -= 1
                dir = 'N'
            else:
                sy+=1
                dir = 'S'
            cnt += 1
        elif k == 3:
            if dir == 'N':
                sx += 1
                dir = 'E'
            else:
                sy += 1
                dir = 'S'
            cnt += 1
        elif k == 4:
            if dir == 'N':
                sx -= 1
                dir = 'W'
            else:
                sy += 1
                dir = 'S'
            cnt += 1
        elif k == 5:
            if dir == 'E':
                sy -= 1
                dir = 'N'
            else:
                sx -= 1
                dir = 'W'
            cnt += 1
        elif k == 6:
            if dir == 'S':
                sx += 1
                dir = 'E'
            else:
                sy -= 1
                dir = 'N'
            cnt += 1
        else:
            boool = False
            break
    if boool:
        if sy == N-1 and sx == N:
            results.append(cnt)


def go(n, maap, visited):
    global pipes, results
    #print('n : ', n)
    #print('pipes :',pipes)
    if n == len(pipes):
        simulate(maap)
        return

    y, x, real_type = pipes[n]
    if pipes[n][2] in [3, 4, 5, 6]:
        for type in [3, 4, 5, 6]:
            if type == 3:
                boool = True
                dy, dx = (y+1, x)
                if 0<=dy<N and 0<=dx<N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [5, 6, 2]:
                    #         boool = False
                else:
                    boool = False
                dy, dx = (y, x+1)
                if 0<=dy<N and 0<=dx<N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [5, 4, 1]:
                    #         boool = False
                else:
                    boool = False
                if boool:
                    visited[y][x] = True
                    maap[y][x] = 3
                    go(n+1, maap, visited)
                    visited[y][x] = False
                    maap[y][x] = real_type
            elif type == 4:
                boool = True
                dy, dx = (y + 1, x)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [5, 6, 2]:
                    #         boool = False
                else:
                    boool = False
                dy, dx = (y, x - 1)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [3, 6, 1]:
                    #         boool = False
                else:
                    boool = False
                if boool:
                    visited[y][x] = True
                    maap[y][x] = 4
                    go(n + 1, maap, visited)
                    visited[y][x] = False
                    maap[y][x] = real_type
            elif type == 5:
                boool = True
                dy, dx = (y - 1, x)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [3, 4, 2]:
                    #         boool = False
                else:
                    boool = False
                dy, dx = (y, x - 1)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [3, 6, 1]:
                    #         boool = False
                else:
                    boool = False
                if boool:
                    visited[y][x] = True
                    maap[y][x] = 5
                    go(n + 1, maap, visited)
                    visited[y][x] = False
                    maap[y][x] = real_type
            else:  # type = 6
                boool = True
                dy, dx = (y - 1, x)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [3, 4, 2]:
                    #         boool = False
                else:
                    boool = False
                dy, dx = (y, x + 1)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [1, 4, 5]:
                    #         boool = False
                else:
                    boool = False
                if boool:
                    visited[y][x] = True
                    maap[y][x] = 6
                    go(n + 1, maap, visited)
                    visited[y][x] = False
                    maap[y][x] = real_type
    else:  # pipes in [1, 2]
        for type in [1, 2]:
            if type == 1:
                boool = True
                dy, dx = (y, x-1)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [3, 6, 1]:
                    #         boool = False
                else:
                    boool = False
                dy, dx = (y, x+1)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [4, 5, 1]:
                    #         boool = False
                else:
                    boool = False
                if boool:
                    visited[y][x] = True
                    maap[y][x] = 1
                    go(n + 1, maap, visited)
                    visited[y][x] = False
                    maap[y][x] = real_type
            else:
                boool = True
                dy, dx = (y-1, x)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [2, 3, 4]:
                    #         boool = False
                else:
                    boool = False
                dy, dx = (y+1, x)
                if 0 <= dy < N and 0 <= dx < N:
                    if maap[dy][dx] == 0:
                        boool = False
                    # elif visited[dy][dx]:
                    #     if maap[dy][dx] not in [2, 5, 6]:
                    #         boool = False
                else:
                    boool = False
                if boool:
                    visited[y][x] = True
                    maap[y][x] = 2
                    go(n + 1, maap, visited)
                    visited[y][x] = False
                    maap[y][x] = real_type











T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(char) for char in input().split()]
        maap.append(temp)
    visited = [[False]*N for _ in range(N)]
    pipes = []

    for i in range(N):
        for j in range(N):
            if maap[i][j] != 0:
                pipes.append([i, j, maap[i][j]])
    sy, sx, skind = pipes.pop(0)
    ey, ex, ekind = pipes.pop()
    results = []

    go(0, maap, visited)
    print(min(results))