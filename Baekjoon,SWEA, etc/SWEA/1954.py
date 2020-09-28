testcases = int(input())
for testcase in range(1, testcases+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    cy, cx = 0, 0
    value = 1
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    o = 0

    while True:
        arr[cy][cx] = value
        value += 1
        visited[cy][cx] = True
        if cy + dy[o] <N and  cx + dx[o] < N and not visited[cy+dy[o]][cx+dx[o]]:
            cy += dy[o]
            cx += dx[o]
            continue
        else:
            boool = False
            for i in range(4):
                o = (o+1)%4
                if cy + dy[o] < N and cx + dx[o] < N and not visited[cy+dy[o]][cx+dx[o]]:
                    boool = True
                    break
            if boool:
                cy += dy[o]
                cx += dx[o]
                continue
            else:
                break

    print('#{}'.format(testcase))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
