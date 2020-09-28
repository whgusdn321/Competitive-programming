def move(y, x, dir):
    if dir == 'E':
        x += 1
    elif dir == 'W':
        x -= 1
    elif dir == 'S':
        y += 1
    else:
        y -= 1
    return y, x


def simulate(y, x ,dir):
    global maap, N, wormholes, results
    sy, sx = y, x
    cy, cx = y, x
    points = 0

    while True:
        cy, cx = move(cy, cx, dir)
        if [cy, cx] == [sy, sx] or (0<=cy<N and 0<=cx<N and maap[cy][cx] == -1):
            break

        if cy < 0:
            dir = 'S'
            points += 1
            continue
        elif cx < 0:
            dir = 'E'
            points += 1
            continue
        elif cx >= N:
            dir = 'W'
            points += 1
            continue
        elif cy >= N:
            dir = 'N'
            points += 1
            continue
        elif maap[cy][cx] == 0:
            continue
        else:
            if maap[cy][cx] == 1:
                if dir == 'N':
                    dir = 'S'
                    points += 1
                elif dir == 'E':
                    dir = 'W'
                    points += 1
                elif dir == 'W':
                    dir = 'N'
                    points += 1
                else:
                    dir = 'E'
                    points += 1
            elif maap[cy][cx] == 2:
                if dir == 'S':
                    dir = 'N'
                    points += 1
                elif dir == 'E':
                    dir = 'W'
                    points += 1
                elif dir == 'W':
                    dir = 'S'
                    points += 1
                else:
                    dir = 'E'
                    points += 1
            elif maap[cy][cx] == 3:
                if dir == 'S':
                    dir = 'N'
                    points += 1
                elif dir == 'W':
                    dir = 'E'
                    points += 1
                elif dir == 'E':
                    dir = 'S'
                    points += 1
                else:
                    dir = 'W'
                    points += 1
            elif maap[cy][cx] == 4:
                if dir == 'W':
                    dir = 'E'
                    points += 1
                elif dir == 'N':
                    dir = 'S'
                    points += 1
                elif dir == 'E':
                    dir = 'N'
                    points += 1
                else:
                    dir = 'W'
                    points += 1
            elif maap[cy][cx] ==5:
                if dir == 'W':
                    dir = 'E'
                    points += 1
                elif dir == 'N':
                    dir = 'S'
                    points += 1
                elif dir == 'E':
                    dir = 'W'
                    points += 1
                else:
                    dir = 'N'
                    points += 1
            else:
                cy, cx = wormholes[(cy, cx)]
    results.append(points)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(char) for char in input().split()]
        maap.append(temp)

    zeros = []
    _wormholes = {6:[], 7:[], 8:[], 9:[], 10:[]}
    wormholes = {}
    for i in range(N):
        for j in range(N):
            if maap[i][j] == 0:
                zeros.append((i, j))
            elif maap[i][j] > 5:
                _wormholes[maap[i][j]].append((i, j))
            else:
                pass
    for item in _wormholes.values():
        if item:
            a, b = item[0], item[1]
            wormholes[a] = b
            wormholes[b] = a

    results = []
    for zy, zx in zeros:
        simulate(zy, zx, 'W')
        simulate(zy, zx, 'N')
        simulate(zy, zx, 'E')
        simulate(zy, zx, 'S')

    print(max(results))