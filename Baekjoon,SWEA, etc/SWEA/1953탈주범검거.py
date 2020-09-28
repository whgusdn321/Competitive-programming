import queue
down = [1, 2, 5, 6]
up = [1, 2, 4, 7]
right = [1, 3, 4, 5]
left = [1, 3, 6, 7]


def inspect(R, C, time):
    global H, W, L, visited, result

    q = queue.Queue()
    q.put([R, C, maap[R][C], 1])
    visited[R][C] = True
    cnt = 1

    while q.qsize() != 0:
        py, px, pkind, ptime = q.get()
        if ptime == time:
            continue
        if pkind == 1:
            dy, dx = py, px-1
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in right and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
            dy, dx = py-1, px
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in down and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
            dy, dx = py, px+1
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in left and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
            dy, dx = py+1, px
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in up and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
        elif pkind == 2:
            dy, dx = py - 1, px
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in down and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
            dy, dx = py + 1, px
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in up and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
        elif pkind == 3:
            dy, dx = py, px - 1
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in right and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1

            dy, dx = py, px + 1
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in left and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
        elif pkind == 4:
            dy, dx = py - 1, px
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in down and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
            dy, dx = py, px + 1
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in left and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
        elif pkind == 5:
            dy, dx = py, px + 1
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in left and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
            dy, dx = py + 1, px
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in up and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
        elif pkind == 6:
            dy, dx = py, px - 1
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in right and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
            dy, dx = py + 1, px
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in up and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
        else:
            dy, dx = py, px - 1
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in right and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
            dy, dx = py - 1, px
            if 0 <= dy < H and 0 <= dx < W and maap[dy][dx] in down and not visited[dy][dx]:
                q.put([dy, dx, maap[dy][dx], ptime+1])
                visited[dy][dx] = True
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    H, W, R, C, time = map(int, input().split())
    maap = []
    visited = [[False]*W for _ in range(H)]
    for _ in range(H):
        temp = [int(char) for char in input().split()]
        maap.append(temp)
    #result = 0
    result = inspect(R, C, time)
    print('#{} {}'.format(tc, result))
