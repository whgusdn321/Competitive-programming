def go(y, x, k, cnt):
    global maap, visited, results, N
    visited[y][x] = True
    adj = [(y, x-1), (y-1, x),(y,x+1),(y+1, x)]
    for dy, dx in adj:
        if 0<=dy<N and 0<=dx<N and not visited[dy][dx]:
            if maap[dy][dx] < maap[y][x]:
                go(dy, dx, k, cnt+1)
            else:
                if maap[dy][dx] - k < maap[y][x]:
                    temp = maap[dy][dx]
                    maap[dy][dx] = maap[y][x] - 1
                    go(dy, dx, 0, cnt+ 1)
                    maap[dy][dx] = temp
    visited[y][x] = False
    results.append(cnt)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    maap = []
    for _ in range(N):
        temp = [int(char) for char in input().split()]
        maap.append(temp)
    visited = [[False]*N for _ in range(N)]
    maxs = []
    max_value = -99
    for i in range(N):
        for j in range(N):
            if maap[i][j] > max_value:
                maxs = []
                maxs.append((i, j))
                max_value = maap[i][j]
            elif maap[i][j] == max_value:
                maxs.append((i, j))
            else:
                pass
    results = []
    for py, px in maxs:
        go(py, px, K, 1)
        # print('visited : ')
        # for _ in range(N):
        #     print(visited[_])
    print('#{} {}'.format(tc, max(results)))