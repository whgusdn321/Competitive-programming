import sys
sys.setrecursionlimit(10**9)


def go(y, x, summ):
    global N, maap, visited, result, mins
    if not (0 <= y < N and 0 <= x < N) or visited[y][x] or summ > result:
        return

    if y == N-1 and x == N-1:
        result = min(summ, result)
        return

    summ += maap[y][x]
    visited[y][x] = True

    if summ >= mins[y][x]:
        visited[y][x] = False
        return
    else:
        mins[y][x] = summ
        adjacents = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
        for dy, dx in adjacents:
            go(dy, dx, summ)

        visited[y][x] = False



TC = int(input())
for tc in range(1, TC+1):
    result = 999
    N = int(input())
    maap = []
    visited = []
    mins = []
    for _ in range(N):
        temp = [int(char) for char in input()]
        maap.append(temp)
        temp2 = [False] * N
        visited.append(temp2)
        mins.append([999]*N)

    go(0,0, 0)
    print('#{} {}'.format(tc, result))
    #print('len(results) : ',min(results))