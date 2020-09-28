dirs = {'E':0, 'S':1, 'W':2, 'N':3}
W, H = map(int, input().split())
N, M = map(int, input().split())
robots = [None]
maap = [[0]*W for _ in range(H)]
for _ in range(N):
    x, y, dir = [char for char in input().split()]
    x = int(x)
    y = int(y)
    robots.append([H-y, x-1, dirs[dir]])
    maap[H-y][x-1] = _+1

opers = []
for _ in range(M):
    r, oper, n = [char for char in input().split()]
    opers.append((int(r), oper, int(n)))

boool = True
while boool and opers:
    r, oper, n = opers.pop(0)
    if oper == 'L':
        n = n%4
        robots[r][2] = (robots[r][2] - n)%4
    elif oper == 'R':
        n = n%4
        robots[r][2] = (robots[r][2] + n)%4
    else:
        ry, rx, dir = robots[r]
        boool2 = True
        if dir == 0:  # East
            for _ in range(n):
                ny, nx = ry, rx+1
                if not(0<=ny<H and 0<=nx<W):
                    print('Robot {} crashes into the wall'.format(r))
                    boool2 = False
                    break
                elif maap[ny][nx] != 0:
                    print('Robot {} crashes into robot {}'.format(r, maap[ny][nx]))
                    boool2 = False
                    break
                else:
                    maap[ny][nx] = maap[ry][rx]
                    maap[ry][rx] = 0
                    ry, rx = ny, nx
        elif dir == 1:  # south
            for _ in range(n):
                ny, nx = ry+1, rx
                if not (0 <= ny < H and 0 <= nx < W):
                    print('Robot {} crashes into the wall'.format(r))
                    boool2 = False
                    break
                elif maap[ny][nx] != 0:
                    print('Robot {} crashes into robot {}'.format(r, maap[ny][nx]))
                    boool2 = False
                    break
                else:
                    maap[ny][nx] = maap[ry][rx]
                    maap[ry][rx] = 0
                    ry, rx = ny, nx
        elif dir == 2:  # West
            for _ in range(n):
                ny, nx = ry, rx - 1
                if not (0 <= ny < H and 0 <= nx < W):
                    print('Robot {} crashes into the wall'.format(r))
                    boool2 = False
                    break
                elif maap[ny][nx] != 0:
                    print('Robot {} crashes into robot {}'.format(r, maap[ny][nx]))
                    boool2 = False
                    break
                else:
                    maap[ny][nx] = maap[ry][rx]
                    maap[ry][rx] = 0
                    ry, rx = ny, nx
        else:
            for _ in range(n):
                ny, nx = ry - 1, rx
                if not (0 <= ny < H and 0 <= nx < W):
                    print('Robot {} crashes into the wall'.format(r))
                    boool2 = False
                    break
                elif maap[ny][nx] != 0:
                    print('Robot {} crashes into robot {}'.format(r, maap[ny][nx]))
                    boool2 = False
                    break
                else:
                    maap[ny][nx] = maap[ry][rx]
                    maap[ry][rx] = 0
                    ry, rx = ny, nx
        if boool2:
            robots[r] = [ry, rx, dir]
            continue
        else:
            boool = False
            break

if boool:
    print('OK')


