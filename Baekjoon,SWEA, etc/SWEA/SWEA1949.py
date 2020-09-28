import sys
read = lambda: input()

test_cases = int(read())


def go(y, x, k, cnt):
    global cnts, N, maap, visited
    cnt += 1
    adj = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adj:
        if 0 <= dy < N and 0 <= dx < N:
            if maap[dy][dx] < maap[y][x]:
                visited[dy][dx] = True
                go(dy, dx, k, cnt)
                visited[dy][dx] = False
            else:
                for kk in range(1, k+1):
                    if maap[dy][dx] - kk < maap[y][x] and not visited[dx][dy]:
                        maap[dy][dx] -= kk
                        visited[dy][dx] = True
                        go(dy, dx, 0, cnt)
                        visited[dy][dx] = False
                        maap[dy][dx] += kk
                        break
    cnts.append(cnt)


for test_case in range(1, test_cases+1):
    N, k = map(int, read().split())
    maap = []

    for _ in range(N):
        temp = [int(a) for a in read().split()]
        maap.append(temp)

    max_heights = []
    maxi, maxj = 0, 0
    for i in range(N):
        for j in range(N):
            if maap[i][j] > maap[maxi][maxj]:
                max_heights = []
                max_heights.append((i, j))
                maxi, maxj = i, j
            elif maap[i][j] == maap[maxi][maxj]:
                max_heights.append((i, j))

    real_cnts = []
    for max_height in max_heights:
        cnts = []
        visited = [['False'] *N for _ in range(N)]
        visited[max_height[0]][max_height[1]] = True
        go(max_height[0],max_height[1], k, 0)
        real_cnts.append(max(cnts))
    print('#{} {}'.format(test_case, max(real_cnts)))



