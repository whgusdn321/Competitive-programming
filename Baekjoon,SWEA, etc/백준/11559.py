import sys
sys.setrecursionlimit(1000000000)
read = lambda :sys.stdin.readline().rstrip()

H = 12
W = 6
maap = []
for _ in range(H):
    temp = [a for a in read()]
    maap.append(temp)


def go(y, x, color):
    global visited, maap, stack
    visited[y][x] = True
    stack.append((y, x))
    adjacent = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adjacent:
        if 0<=dy<H and 0<=dx<W and not visited[dy][dx] and maap[dy][dx] == color:
            go(dy, dx, color)


def gravity(maap):
    for x in range(6):
        temp = []
        for y in range(12):
            temp.append(maap[y][x])
        temp2= ['.'] * 12

        k = 1
        for i in range(-1, -13, -1):
            if temp[i] != '.':
                temp2[-k] = temp[i]
                k+=1
        for y in range(12):
            maap[y][x] = temp2[y]

k = 0
while True:
    flag = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(H):
        for j in range(W):
            if maap[i][j] != '.' and not visited[i][j]:
                stack = []
                go(i, j, maap[i][j])
                if len(stack) >= 4:
                    for yy, xx in stack:
                        maap[yy][xx] = '.'
                        flag = True
    if flag:
        k += 1
    else:
        break

    # print('before gravity : ' )
    # for _ in range(12):
    #     print(maap[_])

    gravity(maap)

    # print('after gravity : ')
    # for _ in range(12):
    #     print(maap[_])
print(k)