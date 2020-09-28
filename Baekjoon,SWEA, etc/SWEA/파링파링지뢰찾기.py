def go(y, x):
    global visited, maap2
    if visited[y][x] : return
    if maap2[y][x] == -1:
        return
    if maap2[y][x] >= 1:
        visited[y][x] = True
        return
    visited[y][x] = True
    adj = [(y, x - 1), (y - 1, x), (y, x + 1), (y + 1, x), (y - 1, x - 1), (y - 1, x + 1), (y + 1, x - 1),
           (y + 1, x + 1)]
    for dy, dx in adj:
        if 0<=dy<N and 0<=dx<N:
            go(dy, dx)


def calculate(maap, i, j):
    global N
    cnt = 0
    if maap[i][j] == '*':
        return -1
    adj = [(i, j-1), (i-1, j), (i, j+1), (i+1, j), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for dy, dx in adj :
        if 0<=dy<N and 0<=dx<N:
            if maap[dy][dx] =='*':
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = input()
        maap.append(temp)
    maap2 = []
    zeros = []
    elses = []
    for i in range(N):
        temp = []
        for j in range(N):
            a = calculate(maap, i, j)
            temp.append(a)
            if a == 0:
                zeros.append((i, j))
            elif a != -1:
                elses.append((i, j))
            else:
                pass
        maap2.append(temp)
    # print('maap2 : ')
    # for _ in range(N):
    #     print(maap2[_])
    visited = [[False]*N for _ in range(N)]
    result = 0
    for i, j in zeros:
        if not visited[i][j]:
            go(i, j)
            result += 1
    for i, j in elses:
        if not visited[i][j]:
            go(i, j)
            result += 1
    print('#{} {}'.format(tc, result))

