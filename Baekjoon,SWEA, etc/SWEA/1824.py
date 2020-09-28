from collections import deque


def f(y, x, dir, memory):
    global maap, H, W
    if maap[y][x] == '<':
        ny, nx, dir, memory = y, (x-1)%W, 'W', memory
        return ny, nx, dir, memory
    elif maap[y][x] == '>':
        ny, nx, dir, memory = y, (x+1)%W, 'E', memory
        return ny, nx, dir, memory
    elif maap[y][x] == '^':
        ny, nx, dir, memory = (y-1)%H, x, 'N', memory
        return ny, nx, dir, memory
    elif maap[y][x] == 'v':
        ny, nx, dir, memory = (y + 1) % H, x, 'S', memory
        return ny, nx, dir, memory
    elif maap[y][x] == '_':
        if memory == 0:
            ny, nx, dir, memory = y, (x + 1) % W, 'E', memory
            return ny, nx, dir, memory
        else:
            ny, nx, dir, memory = y, (x - 1) % W, 'W', memory
            return ny, nx, dir, memory
    elif maap[y][x] == '|':
        if memory == 0:
            ny, nx, dir, memory = (y + 1) % H, x, 'S', memory
            return ny, nx, dir, memory
        else:
            ny, nx, dir, memory = (y - 1) % H, x, 'N', memory
            return ny, nx, dir, memory
    elif maap[y][x] == '?':
        ny1, nx1, dir1, memory1 = y, (x - 1) % W, 'W', memory
        ny2, nx2, dir2, memory2 = y, (x + 1) % W, 'E', memory
        ny3, nx3, dir3, memory3 = (y - 1) % H, x, 'N', memory
        ny4, nx4, dir4, memory4 = (y + 1) % H, x, 'S', memory
        return [ny1, nx1, dir1, memory1], [ny2, nx2, dir2, memory2], \
               [ny3, nx3, dir3, memory3], [ny4, nx4, dir4, memory4],
    elif maap[y][x] == '.':
        if dir == 'N':
            ny, nx, dir, memory = (y - 1) % H, x, 'N', memory
            return ny, nx, dir, memory
        elif dir == 'S':
            ny, nx, dir, memory = (y + 1) % H, x, 'S', memory
            return ny, nx, dir, memory
        elif dir == 'W':
            ny, nx, dir, memory = y, (x - 1) % W, 'W', memory
            return ny, nx, dir, memory
        else:
            ny, nx, dir, memory = y, (x + 1) % W, 'E', memory
            return ny, nx, dir, memory

    elif maap[y][x] == '@':
        None
    elif maap[y][x] in ['0','1','2','3','4','5','6','7','8','9']:
        if dir == 'N':
            ny, nx, dir, memory = (y - 1) % H, x, 'N', int(maap[y][x])
            return ny, nx, dir, memory
        elif dir == 'S':
            ny, nx, dir, memory = (y + 1) % H, x, 'S', int(maap[y][x])
            return ny, nx, dir, memory
        elif dir == 'W':
            ny, nx, dir, memory = y, (x - 1) % W, 'W', int(maap[y][x])
            return ny, nx, dir, memory
        else:
            ny, nx, dir, memory = y, (x + 1) % W, 'E', int(maap[y][x])
            return ny, nx, dir, memory
    elif maap[y][x] == '+':
        if memory == 15:
            if dir == 'N':
                ny, nx, dir, memory = (y - 1) % H, x, 'N', 0
                return ny, nx, dir, memory
            elif dir == 'S':
                ny, nx, dir, memory = (y + 1) % H, x, 'S', 0
                return ny, nx, dir, memory
            elif dir == 'W':
                ny, nx, dir, memory = y, (x - 1) % W, 'W', 0
                return ny, nx, dir, memory
            else:
                ny, nx, dir, memory = y, (x + 1) % W, 'E', 0
                return ny, nx, dir, memory
        else:
            if dir == 'N':
                ny, nx, dir, memory = (y - 1) % H, x, 'N', memory
                return ny, nx, dir, memory+1
            elif dir == 'S':
                ny, nx, dir, memory = (y + 1) % H, x, 'S', memory
                return ny, nx, dir, memory+1
            elif dir == 'W':
                ny, nx, dir, memory = y, (x - 1) % W, 'W', memory
                return ny, nx, dir, memory+1
            else:
                ny, nx, dir, memory = y, (x + 1) % W, 'E', memory
                return ny, nx, dir, memory+1
    elif maap[y][x] == '-':
        if memory == 0:
            if dir == 'N':
                ny, nx, dir, memory = (y - 1) % H, x, 'N', 15
                return ny, nx, dir, memory
            elif dir == 'S':
                ny, nx, dir, memory = (y + 1) % H, x, 'S', 15
                return ny, nx, dir, memory
            elif dir == 'W':
                ny, nx, dir, memory = y, (x - 1) % W, 'W', 15
                return ny, nx, dir, memory
            else:
                ny, nx, dir, memory = y, (x + 1) % W, 'E', 15
                return ny, nx, dir, memory
        else:
            if dir == 'N':
                ny, nx, dir, memory = (y - 1) % H, x, 'N', memory
                return ny, nx, dir, memory-1
            elif dir == 'S':
                ny, nx, dir, memory = (y + 1) % H, x, 'S', memory
                return ny, nx, dir, memory-1
            elif dir == 'W':
                ny, nx, dir, memory = y, (x - 1) % W, 'W', memory
                return ny, nx, dir, memory-1
            else:
                ny, nx, dir, memory = y, (x + 1) % W, 'E', memory
                return ny, nx, dir, memory-1



testcases = int(input())
for testcase in range(1, testcases+1):
    H, W = map(int, input().split())
    maap = []
    for _ in range(H):
        maap.append(input())

    history = [[[] for _ in range(W)] for _ in range(H)]
    queue = deque([(0, 0, 'E', 0)])
    boool = False
    while queue:
        y, x, dir, memory = queue.popleft()
        if (dir, memory) in history[y][x]:
            continue
        history[y][x].append((dir, memory))
        if maap[y][x] == '@':
            boool = True
            break
        ny, nx, ndir, towrite = f(y, x, dir, memory)
        if isinstance(ny, list):
            ny1, nx1, ndir1, towrite1 = ny
            ny2, nx2, ndir2, towrite2 = nx
            ny3, nx3, ndir3, towrite3 = ndir
            ny4, nx4, ndir4, towrite4 = towrite
            queue.append((ny1, nx1, ndir1, towrite1))
            queue.append((ny2, nx2, ndir2, towrite2))
            queue.append((ny3, nx3, ndir3, towrite3))
            queue.append((ny4, nx4, ndir4, towrite4))
        else:
            queue.append((ny, nx, ndir, towrite))

    if boool:
        print('#{} YES'.format(testcase))
    else:
        print('#{} NO'.format(testcase))
