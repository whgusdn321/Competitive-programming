def expand(maap):
    global H, W
    temp = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if maap[i][j] > 0:
                adj = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
                cnt = 0
                for dy, dx in adj:
                    if 0<=dy<H and 0<=dx<W and maap[dy][dx] != -1:
                        cnt += 1
                        temp[dy][dx] += maap[i][j]//5
                maap[i][j] = maap[i][j] - (maap[i][j]//5) * cnt
    for i in range(H):
        for j in range(W):
            maap[i][j] += temp[i][j]


def cleanAir(maap, ay, ax, by, bx):
    global H
    trace = []
    values = []
    cy, cx = ay, ax

    dy, dx = (0, 1)
    for _ in range(W-1):
        cy += dy
        cx += dx
        trace.append((cy, cx))
        values.append(maap[cy][cx])

    dy, dx = (-1, 0)
    for _ in range(ay):
        cy += dy
        cx += dx
        trace.append((cy, cx))
        values.append(maap[cy][cx])

    dy, dx = (0, -1)
    for _ in range(W - 1):
        cy += dy
        cx += dx
        trace.append((cy, cx))
        values.append(maap[cy][cx])

    dy, dx = (1, 0)
    for _ in range(ay):
        cy += dy
        cx += dx
        trace.append((cy, cx))
        values.append(maap[cy][cx])

    for j in range(len(trace)):
        cy, cx = trace[j]
        beforev = values[(j-1)%len(trace)]
        if beforev == -1:
            maap[cy][cx] = 0
        else:
            maap[cy][cx] = beforev

    maap[ay][ax] = -1

    trace = []
    values = []
    cy, cx = by, bx

    dy, dx = (0, 1)
    for _ in range(W - 1):
        cy += dy
        cx += dx
        trace.append((cy, cx))
        values.append(maap[cy][cx])

    dy, dx = (1, 0)
    for _ in range(H-by-1):
        cy += dy
        cx += dx
        trace.append((cy, cx))
        values.append(maap[cy][cx])

    dy, dx = (0, -1)
    for _ in range(W - 1):
        cy += dy
        cx += dx
        trace.append((cy, cx))
        values.append(maap[cy][cx])

    dy, dx = (-1, 0)
    for _ in range(H-by-1):
        cy += dy
        cx += dx
        trace.append((cy, cx))
        values.append(maap[cy][cx])

    for j in range(len(trace)):
        cy, cx = trace[j]
        beforev = values[(j - 1) % len(trace)]
        if beforev == -1:
            maap[cy][cx] = 0
        else:
            maap[cy][cx] = beforev

    maap[by][bx] = -1




H, W, T = map(int, input().split())
maap = []
for _ in range(H):
    temp = [int(char) for char in input().split()]
    maap.append(temp)

ayax = []

for i in range(H):
    for j in range(W):
        if maap[i][j] == -1:
            ayax.append((i, j))

for t in range(T):
    expand(maap)
    cleanAir(maap, ayax[0][0], ayax[0][1], ayax[1][0], ayax[1][1])

cnt = 0
for i in range(H):
    for j in range(W):
        if maap[i][j] != -1:
            cnt += maap[i][j]
print(cnt)