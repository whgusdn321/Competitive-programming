import sys
from collections import deque
from copy import deepcopy
read = lambda:sys.stdin.readline().rstrip()

H, W = map(int, read().split())
maap = []

for _ in range(H):
    temp = [int(a) for a in read().split()]
    maap.append(temp)

zeros = []
for i in range(H):
    for j in range(W):
        if maap[i][j] == 0:
            zeros.append((i, j))

combis = []


def combi(i, stack, goal):
    global zeros, combis
    if len(stack) == goal:
        combis.append(stack.copy())
        return
    else:
        for j in range(i+1, len(zeros)):
            stack.append(j)
            combi(j, stack, goal)
            stack.pop()

combi(-1, [], 3)


def bfs(y, x):
    global maaap, visited, H, W
    queue = deque([(y, x)])
    visited[y][x] = True
    maaap[y][x] = 2

    while queue:
        py, px = queue.popleft()
        adj = [(py, px-1), (py-1, px), (py, px+1), (py+1, px)]
        for dy, dx in adj:
            if 0<=dy<H and 0<=dx<W and not visited[dy][dx]:
                if maaap[dy][dx] == 0:
                    visited[dy][dx] = True
                    queue.append((dy, dx))
                    maaap[dy][dx] = 2
    return

cnts = []
for combi in combis:
    maaap = deepcopy(maap)
    zero1 = zeros[combi[0]]
    zero2 = zeros[combi[1]]
    zero3 = zeros[combi[2]]
    maaap[zero1[0]][zero1[1]] = 1
    maaap[zero2[0]][zero2[1]] = 1
    maaap[zero3[0]][zero3[1]] = 1

    visited = [[False] * W for _ in range(H)]


    for i in range(H):
        for j in range(W):
            if maaap[i][j] == 2 and not visited[i][j]:
                bfs(i, j)
    cnt = 0
    for i in range(H):
        for j in range(W):
            if maaap[i][j] == 0:
                cnt += 1
    cnts.append(cnt)
#print('cnts : ', cnts)
print(max(cnts))


