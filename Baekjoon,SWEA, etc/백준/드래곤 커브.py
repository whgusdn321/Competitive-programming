def move(y, x, dir):
    if dir == 0: #right
        ny, nx = y, x + 1
    elif dir == 1: #up
        ny, nx = y-1, x
    elif dir == 2: #left
        ny, nx = y, x-1
    else:
        ny, nx = y+1, x
    return ny, nx

maap = [[0]*101 for _ in range(101)]
cy, cx = None, None

n = int(input())
curves = []

for _ in range(n):
    x, y, dir, g = map(int, input().split())
    curves.append([x, y, dir, g])

for dragon_curve in curves:
    x, y, dir, g = dragon_curve
    maap[y][x] = 1
    arr = []
    cy, cx = move(y, x, dir)
    maap[cy][cx] = 1
    arr.append(dir)

    for _ in range(g):
        for i in range(len(arr)-1, -1, -1):
            dir = arr[i]
            if dir == 0:
                cy, cx = move(cy, cx, 1)
                if 0<=cy<101 and 0<=cx<101:
                    maap[cy][cx] = 1
                arr.append(1)
            elif dir == 1:
                cy, cx = move(cy, cx, 2)
                if 0 <= cy < 101 and 0 <= cx < 101:
                    maap[cy][cx] = 1
                arr.append(2)
            elif dir == 2:
                cy, cx = move(cy, cx, 3)
                if 0 <= cy < 101 and 0 <= cx < 101:
                    maap[cy][cx] = 1
                arr.append(3)
            else:
                cy, cx = move(cy, cx, 0)
                if 0 <= cy < 101 and 0 <= cx < 101:
                    maap[cy][cx] = 1
                arr.append(0)

#print('after maap :')
#for _ in range(101):
#    print(maap[_])
cnt = 0
for i in range(100):
    for j in range(100):
        if maap[i][j] == 1 and maap[i][j+1] == 1 and maap[i+1][j] == 1 and maap[i+1][j+1] == 1:
            cnt += 1
print(cnt)