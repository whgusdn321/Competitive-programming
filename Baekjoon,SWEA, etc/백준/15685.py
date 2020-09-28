import sys
read = lambda :sys.stdin.readline().rstrip()


maap = [[False]*101 for _ in range(101)]
curves = int(read())
for curve in range(curves):
    sx, sy, d, g = [int(a) for a in read().split()]
    maap[sy][sx] = True
    #print(sy, sx)
    if d == 0:
        sx += 1
    elif d==1:
        sy -= 1
    elif d==2:
        sx -= 1
    else:
        sy += 1

    maap[sy][sx] = True
    #print(sy, sx)
    cy, cx = sy, sx
    arr = [[cy, cx, d]]

    for gen in range(g):
        for i in range(len(arr)-1, -1, -1):
            dir = arr[i][2]
            if dir == 0:
                ny, nx = cy-1, cx
                if 0 <= ny < 101 and 0 <= nx < 101:
                    maap[ny][nx] = True
                ndir = 1
                arr.append([ny, nx, ndir])
                cy, cx = ny, nx
            if dir == 1:
                ny, nx = cy, cx - 1
                if 0 <= ny < 101 and 0 <= nx < 101:
                    maap[ny][nx] = True
                ndir = 2
                arr.append([ny, nx, ndir])
                cy, cx = ny, nx
            if dir == 2:
                ny, nx = cy + 1, cx
                if 0 <= ny < 101 and 0 <= nx < 101:
                    maap[ny][nx] = True
                ndir = 3
                arr.append([ny, nx, ndir])
                cy, cx = ny, nx
            if dir == 3:
                ny, nx = cy, cx + 1
                if 0 <= ny < 101 and 0 <= nx < 101:
                    maap[ny][nx] = True
                ndir = 0
                arr.append([ny, nx, ndir])
                cy, cx = ny, nx
            #print('cy:{} , cx: {}'.format(cy, cx))
    #for _ in range(101):
    #    print('map : ',maap[_])

cnt = 0
for i in range(100):
    for j in range(100):
       if maap[i][j] == True and maap[i][j+1] == True\
           and maap[i+1][j] == True and maap[i+1][j+1]==True:
           cnt += 1
print(cnt)
