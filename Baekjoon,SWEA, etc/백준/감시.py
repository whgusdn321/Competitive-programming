from copy import deepcopy


def draw(maap, y, x, dir):
    global H, W
    if dir == 'left':
        sy, sx = y, x-1 #
        while sx >=0 and maap[sy][sx] != '6':#
            maap[sy][sx] = '#'
            sx -= 1 #
        return maap
    elif dir == 'right':
        sy, sx = y, x + 1  #
        while sx < W and maap[sy][sx] != '6':  #
            maap[sy][sx] = '#'
            sx += 1  #
        return maap  #
    elif dir == 'up':
        sy, sx = y-1, x
        while sy >= 0 and maap[sy][sx] != '6':
            maap[sy][sx] = '#'
            sy -= 1
        return maap
    else:
        sy, sx = y + 1, x
        while sy < H and maap[sy][sx] != '6':
            maap[sy][sx] = '#'
            sy += 1
        return maap


def go(i, maap):
    global cctvs, results
    if i == len(cctvs):
        result = 0
        for ii in range(H):
            for jj in range(W):
                if maap[ii][jj] == '0':
                    result += 1
        results.append(result)
        return

    cy, cx, kind = cctvs[i]
    if kind == 1:
        maap2 = draw(deepcopy(maap), cy, cx, 'left')
        go(i+1, maap2)

        maap2 = draw(deepcopy(maap), cy,cx,'up')
        go(i+1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'right')
        go(i+1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'down')
        go(i+1, maap2)

    elif kind == 2:
        maap2 = draw(deepcopy(maap), cy, cx, 'left')
        maap2 = draw(maap2, cy, cx, 'right')
        go(i+1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'up')
        maap2 = draw(maap2, cy, cx, 'down')
        go(i + 1, maap2)

    elif kind == 3:
        maap2 = draw(deepcopy(maap), cy, cx, 'up')
        maap2 = draw(maap2, cy, cx, 'right')
        go(i+1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'right')
        maap2 = draw(maap2, cy, cx, 'down')
        go(i + 1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'down')
        maap2 = draw(maap2, cy, cx, 'left')
        go(i + 1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'left')
        maap2 = draw(maap2, cy, cx, 'up')
        go(i + 1, maap2)

    elif kind == 4:
        maap2 = draw(deepcopy(maap), cy, cx, 'up')
        maap2 = draw(maap2, cy, cx, 'left')
        maap2 = draw(maap2, cy, cx, 'right')
        go(i+1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'up')
        maap2 = draw(maap2, cy, cx, 'right')
        maap2 = draw(maap2, cy, cx, 'down')
        go(i + 1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'right')
        maap2 = draw(maap2, cy, cx, 'down')
        maap2 = draw(maap2, cy, cx, 'left')
        go(i + 1, maap2)

        maap2 = draw(deepcopy(maap), cy, cx, 'up')
        maap2 = draw(maap2, cy, cx, 'left')
        maap2 = draw(maap2, cy, cx, 'down')
        go(i + 1, maap2)

    elif kind == 5:
        maap2 = draw(deepcopy(maap), cy, cx, 'up')
        maap2 = draw(maap2, cy, cx, 'left')
        maap2 = draw(maap2, cy, cx, 'right')
        maap2 = draw(maap2, cy, cx, 'down')
        go(i + 1, maap2)


H, W = map(int, input().split())
maap = []
for _ in range(H):
    temp = [char for char in input().split()]
    maap.append(temp)

cctvs = []
for i in range(H):
    for j in range(W):
        if maap[i][j] == '1':
            cctvs.append((i, j, 1))
        elif maap[i][j] == '2':
            cctvs.append((i, j, 2))
        elif maap[i][j] == '3':
            cctvs.append((i, j, 3))
        elif maap[i][j] == '4':
            cctvs.append((i, j, 4))
        elif maap[i][j] == '5':
            cctvs.append((i, j, 5))
        else:
            pass
results = []
go(0, maap)
print(min(results))
