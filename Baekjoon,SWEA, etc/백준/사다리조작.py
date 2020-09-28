import sys


def simulate(maap):
    global H, W, people
    for p in people:
        py = 0
        px = p
        while py < H:
            if maap[py][px] == 1:
                px -= 1
                py += 1
                continue
            elif px+1 < W and maap[py][px+1] == 1:
                px += 1
                py += 1
                continue
            else: # maap[py][px] ==
                py += 1
                continue
        if px != p:
            return False
    return True


def isPossible(maap, i, j):
    global H, W
    if j == 0:
        return False
    elif j == W - 1:
        if maap[i][j-1] == 1:
            return False
        else:
            return True
    else:
        if maap[i][j-1] == 0 and maap[i][j+1] == 0:
            return True
        else:
            return False


def make_combis(i, limit, stakk):
    global N, zeros, combis
    if len(stakk) == limit:
        if limit == 1:
            combis[0].append(stakk.copy())
        elif limit == 2:
            combis[1].append(stakk.copy())
        else:
            combis[2].append(stakk.copy())
        return
    for j in range(i+1, N):
        stakk.append(j)
        make_combis(j, limit, stakk)
        stakk.pop()



W, n, H = map(int, input().split())
maap = [[0] * W for _ in range(H)]
for _ in range(n):
    a, b = map(int, input().split())
    maap[a-1][b] = 1

zeros = []
for i in range(H):
    for j in range(W):
        if maap[i][j] == 0:
            zeros.append((i, j))
N = len(zeros)
combis = [[],[],[]]
make_combis(-1, 1, [])
make_combis(-1, 2, [])
make_combis(-1, 3, [])


zero = False
one = False
two = False
three = False
people = [i for i in range(W)]

if simulate(maap):
    zero = True
    print(0)
    sys.exit(0)

## one
make_combis(-1, 1, [])
for a in combis[0]:
    y, x = zeros[a[0]]
    if isPossible(maap, y, x):
        maap[y][x] = 1
        one |= simulate(maap)
        maap[y][x] = 0
    if one:
        print(1)
        sys.exit(0)

make_combis(-1, 2, [])
## two
for a, b in combis[1]:
    y1, x1 = zeros[a]
    y2, x2 = zeros[b]
    if isPossible(maap, y1, x1):
        maap[y1][x1] = 1
        if isPossible(maap, y2, x2):
            maap[y2][x2] = 1
            two |= simulate(maap)
            maap[y2][x2] = 0
        maap[y1][x1] = 0
    if two:
        print(2)
        sys.exit(0)


make_combis(-1, 3, [])
## three
for a, b, c in combis[2]:
    y1, x1 = zeros[a]
    y2, x2 = zeros[b]
    y3, x3 = zeros[c]
    if isPossible(maap, y1, x1):
        maap[y1][x1] = 1
        if isPossible(maap, y2, x2):
            maap[y2][x2] = 1
            if isPossible(maap, y3, x3):
                maap[y3][x3] = 1
                three |= simulate(maap)
                maap[y3][x3] = 0
            maap[y2][x2] = 0
        maap[y1][x1] = 0
    if three:
        print(3)
        sys.exit(0)


print(-1)
