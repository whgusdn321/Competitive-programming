import sys
from collections import deque

H, W, x, y, k = map(int, sys.stdin.readline().split())
maap = []
for _ in range(H):
    temp = [int(a) for a in sys.stdin.readline().split()]
    maap.append(temp)
opers = deque([int(a) for a in sys.stdin.readline().split()])
#print(' opers : ',opers)
a = [0, 0, 0, 0]
b = [0, 0, 0, 0]


def nextcube(oper):
    global a, b
    temp = [0]*4
    if oper == 4:
        for i in range(4):
            temp[i] = a[(i-1)%4]
        a = temp
        b[0] = a[0]
        b[2] = a[2]
    elif oper == 3:
        for i in range(4):
            temp[i] = a[(i+1)%4]
        a = temp
        b[0] = a[0]
        b[2] = a[2]
    elif oper == 2:
        for i in range(4):
            temp[i] = b[(i+1)%4]
        b = temp
        a[0] = b[0]
        a[2] = b[2]
    else:
        for i in range(4):
            temp[i] = b[(i-1)%4]
        b = temp
        a[0] = b[0]
        a[2] = b[2]

c_y, c_x = x, y
while opers:
    oper = opers.popleft()
    if oper == 4:
        c_y, c_x = c_y+1, c_x
        if not (0 <= c_y < H and 0 <= c_x <W):
            c_y, c_x = c_y-1, c_x
            continue
        else:
            nextcube(oper)
        if maap[c_y][c_x] == 0:
            maap[c_y][c_x] = a[2]
        else:
            a[2] = maap[c_y][c_x]
            b[2] = maap[c_y][c_x]
            maap[c_y][c_x] = 0

    elif oper == 3:
        c_y, c_x = c_y-1, c_x
        if not (0 <= c_y < H and 0 <= c_x < W):
            c_y, c_x = c_y+1, c_x
            continue
        else:
            nextcube(oper)
        if maap[c_y][c_x] == 0:
            maap[c_y][c_x] = a[2]
        else:
            a[2] = maap[c_y][c_x]
            b[2] = maap[c_y][c_x]
            maap[c_y][c_x] = 0

    elif oper == 2:
        c_y, c_x = c_y, c_x-1
        if not (0 <= c_y < H and 0 <= c_x < W):
            c_y, c_x = c_y, c_x+1
            continue
        else:
            nextcube(oper)
        if maap[c_y][c_x] == 0:
            maap[c_y][c_x] = a[2]
        else:
            a[2] = maap[c_y][c_x]
            b[2] = maap[c_y][c_x]
            maap[c_y][c_x] = 0

    elif oper == 1:
        c_y, c_x = c_y, c_x+1
        if not (0 <= c_y < H and 0 <= c_x < W):
            c_y, c_x = c_y, c_x-1
            continue
        else:
            nextcube(oper)
        if maap[c_y][c_x] == 0:
            maap[c_y][c_x] = a[2]
        else:
            a[2] = maap[c_y][c_x]
            b[2] = maap[c_y][c_x]
            maap[c_y][c_x] = 0
    print(b[0])