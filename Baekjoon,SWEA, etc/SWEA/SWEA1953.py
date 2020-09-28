read = lambda : input()
from collections import deque

test_cases = int(read())


def bfs(y, x):
    global maap, visited, time
    visited[y][x] = True
    queue = deque([(y, x, 1)])
    cnt = 0
    while queue:
        py, px, ptime = queue.popleft()
        cnt += 1
        if maap[py][px] == 1:
            adj = []
            if 0<=py<H and 0<=px-1<W and (maap[py][px-1] == 1 or maap[py][px-1] == 3 or maap[py][px-1] == 4 or maap[py][px-1] == 5): #우
                adj.append((py, px-1))
            if 0<=py-1<H and 0<=px<W and (maap[py-1][px] == 1 or maap[py-1][px] == 2 or maap[py-1][px] == 5 or maap[py-1][px] == 6): #하
                adj.append((py-1, px))
            if 0<=py<H and 0<=px+1<W and (maap[py][px+1] == 1 or maap[py][px+1] == 3 or maap[py][px+1] == 6 or maap[py][px+1] == 7): #좌
                adj.append((py, px+1))
            if 0<=py+1<H and 0<=px<W and (maap[py+1][px] == 1 or maap[py+1][px] == 2 or maap[py+1][px] == 4 or maap[py+1][px] == 7): #상
                adj.append((py+1, px))

        elif maap[py][px] == 2:
            adj = []
            if 0<=py-1<H and (maap[py-1][px] == 1 or maap[py-1][px] == 2 or maap[py-1][px] == 5 or maap[py-1][px] == 6): #하
                adj.append((py-1, px))
            if 0<=py+1<H and (maap[py+1][px] == 1 or maap[py+1][px] == 2 or maap[py+1][px] == 4 or maap[py+1][px] == 7): #상
                adj.append((py+1, px))

        elif maap[py][px] == 3: #1,3,4,5 우
            adj = []
            if 0<=px-1<W and (maap[py][px-1] == 1 or maap[py][px-1] == 3 or maap[py][px-1] == 4 or maap[py][px-1] == 5):
                adj.append((py, px-1))
            if 0<=px+1<W and (maap[py][px+1] == 1 or maap[py][px+1] == 3 or maap[py][px+1] == 6 or maap[py][px+1] == 7):#좌
                adj.append((py, px+1))

        elif maap[py][px] == 4:
            adj = []
            if 0<=py-1<H and (maap[py-1][px] == 1 or maap[py-1][px] == 2 or maap[py-1][px] == 5 or maap[py-1][px] == 6): #하
                adj.append((py-1, px))
            if 0<=px+1<W and (maap[py][px+1] == 1 or maap[py][px+1] == 3 or maap[py][px+1] == 6 or maap[py][px+1] == 7):#좌
                adj.append((py, px+1))

        elif maap[py][px] == 5:
            adj = []
            if 0 <= py + 1 < H and (maap[py + 1][px] == 1 or maap[py + 1][px] == 2 or maap[py + 1][px] == 4 or \
                    maap[py + 1][px] == 7):  # 상
                adj.append((py + 1, px))
            if 0<=px+1<W and (maap[py][px+1] == 1 or maap[py][px+1] == 3 or maap[py][px+1] == 6 or maap[py][px+1] == 7):#좌
                adj.append((py, px+1))

        elif maap[py][px] == 6:
            adj = []
            if 0 <= py + 1 < H and (maap[py + 1][px] == 1 or maap[py + 1][px] == 2 or maap[py + 1][px] == 4 or \
                    maap[py + 1][px] == 7):  # 상
                adj.append((py + 1, px))
            if 0<=px-1<W and (maap[py][px-1] == 1 or maap[py][px-1] == 3 or maap[py][px-1] == 4 or maap[py][px-1] == 5):
                adj.append((py, px-1)) #우

        elif maap[py][px] == 7:
            adj = []
            if 0<=py-1<H and (maap[py-1][px] == 1 or maap[py-1][px] == 2 or maap[py-1][px] == 5 or maap[py-1][px] == 6): #하
                adj.append((py-1, px))
            if 0<=px-1<W and (maap[py][px-1] == 1 or maap[py][px-1] == 3 or maap[py][px-1] == 4 or maap[py][px-1] == 5):
                adj.append((py, px-1))
        else:
            adj = []

        for dy, dx in adj:
            if 0 <= dy < H and 0 <= dx < W and not visited[dy][dx]:
                if ptime < time:
                    visited[dy][dx] = True
                    queue.append((dy, dx, ptime + 1))
    return cnt


for test_case in range(1, test_cases + 1):

    H, W, R, C, time = map(int, read().split())

    maap = []
    for _ in range(H):
        temp = [int(a) for a in read().split()]
        maap.append(temp)

    visited = [[False] * W for _ in range(H)]
    cnt = bfs(R, C)
    print('#{} {}'.format(test_case, cnt))
