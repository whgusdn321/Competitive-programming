def backtrack(l, i, j, cnt):
    global visited, maap, results

    if maap[l][i][j] == 'E':
        results.append(cnt)
        return
    else:
        adjacents = [(l-1, i, j), (l+1, i, j), (l, i-1, j), (l, i+1, j), \
                     (l, i, j-1), (l, i, j+1)]
        for dz, dy, dx in adjacents:
            if 0<=dz<L and 0<=dy<H and 0<=dx<W and not visited[dz][dy][dx]:
                if maap[dz][dy][dx] != '#':
                    visited[dz][dy][dx] = True
                    backtrack(dz, dy, dx, cnt+1)
                    visited[dz][dy][dx] = False

while 1:
    L, H, W = map(int, input().split())
    sz, sy, sx = 0, 0, 0
    if L == 0 and H == 0 and W == 0:
        break
    maap = []
    visited = []
    for l in range(L):
        map2D = []
        visited2D = []
        for h in range(H):
            temp = input()
            for w in range(W):
                if temp[w] == 'S':
                    sz, sy, sx = l, h, w
            map2D.append(temp)
            temp2 = [False] * W
            visited2D.append(temp2)
        input()
        maap.append(map2D)
        visited.append(visited2D)
    results = []
    backtrack(sz, sy, sx, 0)
    if results:
        print('Escaped in {} minute(s)'.format(min(results)))
    else:
        print('Trapped!')



