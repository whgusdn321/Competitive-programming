from copy import deepcopy


def eat(person):
    global eaton, H, maap, sharks

    for h in range(H):
        if maap[h][person] is not None:
            eaton += maap[h][person][-1]
            sharks.remove(maap[h][person])
            maap[h][person] = None
            break


def move():
    global H, W, maap, sharks
    # 1 : 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
    sharks.sort(key=lambda x: x[-1], reverse=True)
    next_shark = []
    next_maap = [[None] * W for __ in range(H)]
    for i in range(len(sharks)):
        sy, sx, sspeed, sdir, ssize = sharks[i]
        togo = sspeed
        if sdir == 4:
            if togo <= sx:
                ny, nx = sy, sx-togo
                ndir = 4
            else:
                togo -= sx
                temp = togo // (W-1)
                togo = togo % (W-1)
                if temp %2 == 0:
                    nx = togo
                    ny = sy
                    ndir = 3
                else:
                    nx = (W-1) - togo
                    ny = sy
                    ndir = 4
        elif sdir == 3:
            if togo <= (W-1) - sx:
                ny, nx = sy, sx + togo
                ndir = 3
            else:
                togo -= (W-1) - sx
                temp = togo // (W - 1)
                togo = togo % (W - 1)
                if temp % 2 == 0:
                    nx = (W - 1) - togo
                    ny = sy
                    ndir = 4
                else:
                    nx = togo
                    ny = sy
                    ndir = 3
        elif sdir == 2:
            if togo <= (H-1) - sy:
                ny, nx = sy + togo, sx
                ndir = 2
            else:
                togo -= (H-1) - sy
                temp = togo // (H-1)
                togo = togo % (H-1)
                if temp %2 == 0:
                    nx = sx
                    ny = (H-1) - togo
                    ndir = 1
                else:
                    nx = sx
                    ny = togo
                    ndir = 2
        else:
            if togo <= sy:
                ny, nx = sy - togo, sx
                ndir = 1
            else:
                togo -= sy
                temp = togo // (H-1)
                togo = togo % (H - 1)
                if temp % 2 == 0:
                    nx = sx
                    ny = togo
                    ndir = 2
                else:
                    nx = sx
                    ny = (H-1) - togo
                    ndir = 1

        if next_maap[ny][nx] is not None:
            pass
        else:
            #print('hi :', maap[sy][sx])
            next_maap[ny][nx] = (ny, nx, sspeed, ndir, ssize)
            next_shark.append((ny, nx, sspeed, ndir, ssize))
        maap[sy][sx] = None

    maap = next_maap
    #print('maap :')
    # for _ in range(H):
    #     print(maap[_])
    sharks = next_shark



H, W, M = map(int, input().split())
maap = [[None]*W for __ in range(H)]
next_maap = [[None]*W for __ in range(H)]
sharks = []
for _ in range(M):
    sy, sx, sspeed, sdir, ssize = map(int, input().split())
    sy -= 1
    sx -= 1
    maap[sy][sx] = (sy, sx, sspeed, sdir, ssize)
    sharks.append((sy, sx, sspeed, sdir, ssize))

eaton = 0
person = -1
for _ in range(W):
    person += 1
    eat(person)
    move()
print(eaton)
