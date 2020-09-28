from collections import deque

N = int(input())
maap = []
for _ in range(N):
    temp = [int(char) for char in input().split()]
    maap.append(temp)

sy, sx = 0, 0
for i in range(N):
    for j in range(N):
        if maap[i][j] == 9:
            sy = i
            sx = j
ssize = 2
scnt = 0
time = 0


while True:
    q = deque([[sy, sx]])
    visited = [[False]*N for __ in range(N)]
    visited[sy][sx] = True
    eatable = []
    dist = 1
    while q:
        next_q = deque([])
        while q:
            cy, cx = q.popleft()
            adj = [(cy, cx-1), (cy-1, cx), (cy, cx+1), (cy+1, cx)]
            for dy, dx in adj:
                if 0<=dy<N and 0<=dx<N and maap[dy][dx] <= ssize and not visited[dy][dx]:
                    next_q.append((dy, dx))
                    visited[dy][dx] = True
                    if maap[dy][dx] != 0 and maap[dy][dx] < ssize:
                       eatable.append((dy, dx, dist))
                else:
                    pass
        if eatable:
            break
        else:
            q = next_q
            dist += 1

    if eatable:
        eatable.sort(key = lambda x: [x[0], x[1]])
        ey, ex, edist = eatable[0][0], eatable[0][1], eatable[0][2]
        scnt += 1
        time += edist
        if scnt == ssize:
            scnt = 0
            ssize += 1
        maap[sy][sx] = 0
        sy, sx = ey, ex
        maap[sy][sx] = 9
    else:
        print(time)
        break


