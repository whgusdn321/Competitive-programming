import sys
read = lambda:sys.stdin.readline()

H, W, y, x, k = map(int, read().split())
maap = []
for _ in range(H):
    temp = [int(a) for a in read().split()]
    maap.append(temp)

opers = [int(a) for a in read().split()]

cube = [0, 0, 0, 0, 0, 0]

def rotate_cube(cube, oper):
    if oper == 1:
        temp = [cube[0], cube[1], cube[2], cube[5]]
        cube[0] = temp[1]
        cube[1] = temp[2]
        cube[2] = temp[3]
        cube[5] = temp[0]
    elif oper == 2:
        temp = [cube[0], cube[1], cube[2], cube[5]]
        cube[0] = temp[3]
        cube[1] = temp[0]
        cube[2] = temp[1]
        cube[5] = temp[2]
    elif oper == 3:
        temp = [cube[3], cube[1], cube[4], cube[5]]
        cube[3] = temp[1]
        cube[1] = temp[2]
        cube[4] = temp[3]
        cube[5] = temp[0]
    else:
        temp = [cube[3], cube[1], cube[4], cube[5]]
        cube[3] = temp[3]
        cube[1] = temp[0]
        cube[4] = temp[1]
        cube[5] = temp[2]
    return

cy, cx = y, x
for oper in opers:
    if oper == 1:
        ny, nx = cy, cx+1
        if not (0<=ny<H and 0<=nx<W):
            continue
        else:
            cy, cx = ny, nx
            rotate_cube(cube, 1)
            if maap[cy][cx] == 0:
                maap[cy][cx] = cube[5]
            else:
                cube[5] = maap[cy][cx]
                maap[cy][cx] = 0
            print(cube[1])
    elif oper == 2:
        ny, nx = cy, cx - 1
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        else:
            cy, cx = ny, nx
            rotate_cube(cube, 2)
            if maap[cy][cx] == 0:
                maap[cy][cx] = cube[5]
            else:
                cube[5] = maap[cy][cx]
                maap[cy][cx] = 0
            print(cube[1])
    elif oper == 3:
        ny, nx = cy-1, cx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        else:
            cy, cx = ny, nx
            rotate_cube(cube, 3)
            if maap[cy][cx] == 0:
                maap[cy][cx] = cube[5]
            else:
                cube[5] = maap[cy][cx]
                maap[cy][cx] = 0
            print(cube[1])
    else:
        ny, nx = cy+1, cx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        else:
            cy, cx = ny, nx
            rotate_cube(cube, 4)
            if maap[cy][cx] == 0:
                maap[cy][cx] = cube[5]
            else:
                cube[5] = maap[cy][cx]
                maap[cy][cx] = 0
            print(cube[1])

