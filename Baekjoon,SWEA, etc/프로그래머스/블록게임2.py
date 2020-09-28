one = []
two = []
three = []
four = []
five = []


def rain(b):
    h = len(b)
    w = len(b[0])
    for x in range(w):
        for y in range(h):
            if b[y][x] > 0:
                if y > 0:
                    b[y-1][x] = -1
                break


def pr(b):
    for row in b:
        print(row)
    print()


def clean(b, xs):
    h = len(b)
    for x in xs:
        for y in range(h):
            if b[y][x] == -1:
                b[y][x] = 0


def solution(b):
    h = len(b)
    w = len(b[0])
    d1 = [(1, 0), (2, 0), (2, 1)]
    d2 = [(1, 0), (2, 0), (2, -1)]
    d3 = [(1, 0), (1, -1), (1, -2)]
    d4 = [(1, 0), (1, 1), (1, 2)]
    d5 = [(1, 0), (1, -1), (1, 1)]


    # make list
    for i in range(h):
        for j in range(w):
            pos = True
            if b[i][j] == 0:
                continue
            for dy, dx in d1:
                if 0 <= i+dy < h and 0 <= j +dx < w:
                    if b[i+dy][j+dx] != b[i][j]:
                        pos = False
                        break
                    else:
                        pos &= True
                else:
                    pos = False
                    break
            if pos:
                one.append((i, j))

            pos = True
            for dy, dx in d2:
                if 0 <= i + dy < h and 0 <= j + dx < w:
                    if b[i + dy][j + dx] != b[i][j]:
                        pos = False
                        break
                    else:
                        pos &= True
                else:
                    pos = False
                    break
            if pos:
                two.append((i, j))

            pos = True
            for dy, dx in d3:
                if 0 <= i + dy < h and 0 <= j + dx < w:
                    if b[i + dy][j + dx] != b[i][j]:
                        pos = False
                        break
                    else:
                        pos &= True
                else:
                    pos = False
                    break
            if pos:
                three.append((i, j))

            pos = True
            for dy, dx in d4:
                if 0 <= i + dy < h and 0 <= j + dx < w:
                    if b[i + dy][j + dx] != b[i][j]:
                        pos = False
                        break
                    else:
                        pos &= True
                else:
                    pos = False
                    break
            if pos:
                four.append((i, j))

            pos = True
            for dy, dx in d5:
                if 0 <= i + dy < h and 0 <= j + dx < w:
                    if b[i + dy][j + dx] != b[i][j]:
                        pos = False
                        break
                    else:
                        pos &= True
                else:
                    pos = False
                    break
            if pos:
                five.append((i, j))

    ans = 0
    while 1:
        rain(b)
        # pr(b)
        cnt = 0
        for y, x in one:
            if b[y][x+1] == -1 and b[y+1][x+1] == -1:
                cnt += 1
                clean(b, [x, x+1])
                b[y][x] = 0
                for dy, dx in d1:
                    b[y+dy][x+dx] = 0
                b[y][x+1] = 0
                b[y+1][x+1] = 0

        for y, x in two:
            if b[y][x-1] == -1 and b[y+1][x-1] == -1:
                cnt += 1
                clean(b, [x, x-1])
                b[y][x] = 0
                for dy, dx in d2:
                    b[y+dy][x+dx] = 0
                b[y][x - 1] = 0
                b[y + 1][x - 1] = 0

        for y, x in three:
            if b[y][x-1] == -1 and b[y][x-2] == -1:
                cnt += 1
                clean(b, [x, x-1, x-2])
                b[y][x] = 0
                for dy, dx in d3:
                    b[y+dy][x+dx] = 0
                b[y][x - 1] = 0
                b[y][x - 2] = 0

        for y, x in four:
            if b[y][x+1] == -1 and b[y][x+2] == -1:
                cnt += 1
                clean(b, [x, x+1, x+2])
                b[y][x] = 0
                for dy, dx in d4:
                    b[y+dy][x+dx] = 0
                b[y][x + 1] = 0
                b[y][x + 2] = 0

        for y, x in five:
            if b[y][x-1] == -1 and b[y][x+1] == -1:
                cnt += 1
                clean(b, [x, x-1, x+1])
                b[y][x] = 0
                for dy, dx in d5:
                    b[y+dy][x+dx] = 0
                b[y][x - 1] = 0
                b[y][x + 1] = 0

        ans += cnt
        if cnt == 0:
            break
    return ans




print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))