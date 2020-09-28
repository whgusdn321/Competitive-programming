import itertools
from copy import deepcopy


def move(maap):
    global H, W
    boool = False
    for i in range(H-1, -1, -1):
        for j in range(W):
            if maap[i][j] == 1:
                if i < H-1:
                    boool = True
                    maap[i][j] = 0
                    maap[i+1][j] = 1
                else:
                    maap[i][j] = 0
    return boool


def attack(maap, knights):
    global D, result, H, W
    ky = H
    toremove = []
    for kx in knights:
        for r in range(1, D+1):
            boool = False
            sx = kx - r
            sy = ky

            for _ in range(r):
                if 0<=sy<H and 0<=sx<W and maap[sy][sx] == 1:
                    boool = True
                    if (sy, sx) not in toremove:
                        toremove.append((sy, sx))
                        result += 1
                    break
                else:
                    sy -= 1
                    sx += 1
            if boool:
                break
            for _ in range(r):
                if 0<=sy<H and 0<=sx<W and maap[sy][sx] == 1:
                    boool = True
                    if (sy, sx) not in toremove:
                        toremove.append((sy, sx))
                        result += 1
                    break
                else:
                    sy += 1
                    sx += 1
            if boool:
                break
            for _ in range(r):
                if 0<=sy<H and 0<=sx<W and maap[sy][sx] == 1:
                    boool = True
                    if (sy, sx) not in toremove:
                        toremove.append((sy, sx))
                        result += 1
                    break
                else:
                    sy += 1
                    sx -= 1
            if boool:
                break
            for _ in range(r):
                if 0<=sy<H and 0<=sx<W and maap[sy][sx] == 1:
                    boool = True
                    if (sy, sx) not in toremove:
                        toremove.append((sy, sx))
                        result += 1
                    break
                else:
                    sy -= 1
                    sx -= 1
            if boool:
                break
    for ry, rx in toremove:
        maap[ry][rx] = 0



H, W, D  = map(int, input().split())
maaap = []
for _ in range(H):
    temp = [int(char) for char in input().split()]
    maaap.append(temp)

k = [i for i in range(W)]
combis = itertools.combinations(k, 3)
results = []
for knight in combis:
    maap = deepcopy(maaap)
    allabove = True
    result = 0
    while allabove:
        attack(maap, knight)
        allabove = move(maap)
    results.append(result)
print(max(results))