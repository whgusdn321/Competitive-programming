def go(i, j):
    global infos, N, visited

    if infos[i][j] == 2: #지뢰
        return
    if infos[i][j] == 1:
        visited[i][j] = True
        return
    else:
        visited[i][j] = True
        adjs = [(i, j-1), (i-1, j), (i, j+1), (i+1, j), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for dy, dx in adjs:
            if 0<=dy<N and 0<=dx<N and not visited[dy][dx]:
                go(dy, dx)


tcs = int(input())
for tc in range(1, 1+tcs):
    N = int(input())
    maap = []
    visited = []

    for _ in range(N):
        temp = input()
        maap.append(temp)
        temp2 = [False]*N
        visited.append(temp2)

    all_zeros = []
    not_zeros = []
    mines = []
    infos = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maap[i][j] =='*':
                mines.append((i, j))
                infos[i][j] = 2
            else:
                boool = True
                adjacents = [(i, j-1), (i-1, j), (i, j+1), (i+1, j), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
                for ii, jj in adjacents:
                    if 0<=ii<N and 0<=jj<N:
                        if maap[ii][jj] == '*':
                            boool = False
                            break
                if boool:
                    all_zeros.append((i, j))
                    infos[i][j] = 0
                else:
                    not_zeros.append((i, j))
                    infos[i][j] = 1
    cnt = 0
    for y, x in all_zeros:
        if not visited[y][x]:
            go(y,x)
            cnt += 1
    for y, x in not_zeros:
        if not visited[y][x]:
            cnt += 1
    print('#{} {}'.format(tc, cnt))