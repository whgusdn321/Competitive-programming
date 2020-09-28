import queue

for tc in range(1, 11):
    _ = input()
    maap = []
    visited = [[False]*16 for _ in range(16)]
    for _ in range(16):
        temp = [int(char) for char in input()]
        maap.append(temp)
    sy, sx = 0, 0
    ey, ex = 0, 0
    for i in range(16):
        for j in range(16):
            if maap[i][j] == 2:
                sy, sx = i, j
            elif maap[i][j] == 3:
                ey, ex = i, j
            else:
                pass

    q = queue.Queue()
    visited[sy][sx] = True
    q.put((sy, sx))
    boool = False
    while q.qsize() != 0:
        cy, cx = q.get()
        if [cy, cx] == [ey, ex]:
            boool = True
            break
        adj = [(cy, cx-1), (cy-1, cx), (cy, cx+1), (cy+1, cx)]
        for dy, dx in adj:
            if 0<=dy<16 and 0<=dx<16 and maap[dy][dx] != 1 and not visited[dy][dx]:
                visited[dy][dx] = True
                q.put((dy, dx))
    if boool:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))