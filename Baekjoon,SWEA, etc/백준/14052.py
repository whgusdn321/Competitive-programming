import sys
from copy import deepcopy
H, W = map(int, sys.stdin.readline().split())
maap = []
for y in range(H):
    temp = [int(a) for a in sys.stdin.readline().split()]
    maap.append(temp)

zeros = []
for y in range(H):
    for x in range(W):
        if maap[y][x] == 0:
            zeros.append((y,x))

combis = []


def combi(i, stack):
    global N, zeros, combis
    if len(stack) == 3:
        combis.append(stack.copy())
        return
    for j in range(i+1, len(zeros)):
        stack.append(j)
        combi(j, stack)
        stack.pop()


visited = [False]*len(zeros)
combi(-1, [])


def dfs(y, x, maap, visited):
    visited[y][x] = True
    maap[y][x] = 2
    adjacent = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adjacent:
        if 0<=dy<H and 0<=dx<W:
            if not visited[dy][dx] and maap[dy][dx] == 0:
                dfs(dy, dx, maap, visited)


cnts = []

for combi in combis:
    maap_ = deepcopy(maap)
    visited = [[False] * W for _ in range(H)]
    toone1 = zeros[combi[0]]
    toone2 = zeros[combi[1]]
    toone3 = zeros[combi[2]]

    maap_[toone1[0]][toone1[1]] = 1
    maap_[toone2[0]][toone2[1]] = 1
    maap_[toone3[0]][toone3[1]] = 1

    for i in range(H):
        for j in range(W):
            if not visited[i][j] and maap_[i][j] == 2:
                dfs(i, j, maap_, visited)

    cnt = 0
    for i in range(H):
        for j in range(W):
            if maap_[i][j] == 0:
                cnt += 1
    cnts.append(cnt)

print(max(cnts))