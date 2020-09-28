'''
일딴, 이문제는 전형적인 시뮬래이션 문제이다.
bfs로도 풀 수 있다.
하지만,

'''
def valid(y, x):
    global visited
    if 0 <= y < H and 0 <= x < W and not visited[y][x]:
        return True
    else:
        return False


H, W = map(int, input().split())
visited = [[False] * W for _ in range(H)]
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

cur_y = 0
cur_x = 0
k = 0
cnt = 0

while True:
    visited[cur_y][cur_x] = True
    next_y = cur_y + dy[k]
    next_x = cur_x + dx[k]
    if valid(next_y, next_x):
        cur_y = next_y
        cur_x = next_x
        continue
    else:
        k = (k+1)%4
        next_y = cur_y + dy[k]
        next_x = cur_x + dx[k]
        if valid(next_y, next_x):
            cnt += 1
            cur_y = next_y
            cur_x = next_x
            continue
        else:
            break
print(cnt)