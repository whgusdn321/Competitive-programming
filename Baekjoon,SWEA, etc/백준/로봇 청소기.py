H, W = map(int, input().split())
y, x, dir = map(int, input().split())
maap = []
visited = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(H):
    temp = [int(char) for char in input().split()]
    maap.append(temp)
    temp2 = [False]*W
    visited.append(temp2)

boool = False
cnt = 0

while True:
    if not boool:
        visited[y][x] = True
        cnt += 1
    for i in range(1, 6):
        if i == 5:
            break
        ny = y + dy[(dir-i)%4]
        nx = x + dx[(dir-i)%4]
        if 0 <= ny < H and 0 <= nx < W and maap[ny][nx] == 0 and not visited[ny][nx]:
            y = ny
            x = nx
            dir = (dir-i)%4
            break
    if i != 5:
        boool = False
        continue
    else:
        by = y + dy[(dir-2)%4]
        bx = x + dx[(dir-2)%4]
        if 0 <= by < H and 0 <= bx < W and maap[by][bx] != 1:
            y = y + dy[(dir-2)%4]
            x = x + dx[(dir-2)%4]
            boool = True
            continue
        else:
            break
print(cnt)



