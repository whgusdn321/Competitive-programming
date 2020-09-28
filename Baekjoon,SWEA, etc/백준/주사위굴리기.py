import queue #queuu.put('apple'), queuu.get(), queuu.qsize(),


def move_cube(cube, dirr):
    if dirr == 'E':
        temp = cube[5]
        cube[5] = cube[2]
        cube[2] = cube[1]
        cube[1] = cube[0]
        cube[0] = temp
    elif dirr == 'W':
        temp = cube[1]
        cube[1] = cube[2]
        cube[2] = cube[5]
        cube[5] = cube[0]
        cube[0] = temp
    elif dirr == 'N':
        temp = cube[4]
        cube[4] = cube[5]
        cube[5] = cube[3]
        cube[3] = cube[1]
        cube[1] = temp
    else:
        temp = cube[5]
        cube[5] = cube[4]
        cube[4] = cube[1]
        cube[1] = cube[3]
        cube[3] = temp


H, W, y, x, K = map(int, input().split())
maap = []

for _ in range(H):
    temp = [int(char) for char in input().split()]
    maap.append(temp)

queuu = queue.Queue()
temp = [int(char) for char in input().split()]
for item in temp:
    queuu.put(item)

cube = [0, 0, 0, 0, 0, 0]
while not queuu.empty():
    oper = queuu.get()
    if oper == 1: #east
        if not 0 <= x+1 < W:
            continue
        else:
            x += 1
            move_cube(cube, 'E')
    elif oper == 2:  # west
        if not 0<= x-1 < W:
            continue
        else:
            x -= 1
            move_cube(cube, 'W')
    elif oper == 3:  # North
        if not 0 <= y-1 < H:
            continue
        else:
            y -= 1
            move_cube(cube, 'N')
    else:
        if not 0 <= y+1 < H:
            continue
        else:
            y += 1
            move_cube(cube, 'S')
    if maap[y][x] == 0:
        maap[y][x] = cube[5]
    else:
        cube[5] = maap[y][x]
        maap[y][x] = 0
    print(cube[1])




