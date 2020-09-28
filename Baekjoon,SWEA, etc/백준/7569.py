import sys
from collections import deque

read = lambda :sys.stdin.readline().rstrip()

M, N, H = map(int , read().split())

maap = []


def adjacent(h, y, x):
    adj = [(h, y, x-1), (h, y-1, x), (h, y, x+1), (h, y+1, x),
           (h+1, y, x), (h-1, y, x)]
    return adj


def bfs(ones, maap):
    '''
    이 함수를 돌면 maap에 익을수 있는 토마토들은 1로 변할것이다.
    그리고 visited는 각각의 토마토가 익은 날짜가 들어있을것이다.
    '''

    queue = deque([item + (0,) for item in ones])

    maxdis = 0
    while queue:
        pz, py, px, pdis = queue.popleft()
        if pdis > maxdis :
            maxdis = pdis
        adj = adjacent(pz, py, px)
        for cz, cy, cx in adj:
            if 0<=cz<H and 0<=cy<N and 0<=cx<M:
                if maap[cz][cy][cx] == 0:
                    maap[cz][cy][cx] = 1
                    queue.append((cz, cy, cx, pdis + 1))
    return maxdis


for __ in range(H):
    map2d = []
    for _ in range(N):
        temp = [int(a) for a in read().split()]
        map2d.append(temp)
    maap.append(map2d)

ones = []
for z in range(H):
    for y in range(N):
        for x in range(M):
            if maap[z][y][x] == 1:
                ones.append((z, y, x))

#visited = [[[-1]*M for _ in range(N)] for _ in range(H)]
maxdis = bfs(ones, maap)

flag = False
for z in range(H):
    for y in range(N):
        for x in range(M):
            if maap[z][y][x] == 0:
                flag = True

if flag :
    print(-1)
else:
    print(maxdis)