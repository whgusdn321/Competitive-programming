def make_zeros(maap, y, x, rec):
    if rec == 'one':
        a = 1
    elif rec == 'two':
        a = 2
    elif rec == 'three':
        a = 3
    elif rec == 'four':
        a = 4
    else:
        a = 5
    for _y in range(y, y+a):
        for _x in range(x, x+a):
            #print('_y : {}, _x : {}'.format(_y, _x))
            maap[_y][_x] = 0


def make_ones(maap, y, x, rec):
    if rec == 'one':
        a = 1
    elif rec == 'two':
        a = 2
    elif rec == 'three':
        a = 3
    elif rec == 'four':
        a = 4
    else:
        a = 5
    for _y in range(y, y + a):
        for _x in range(x, x + a):
            maap[_y][_x] = 1


def is_possible(maap, y, x, rec):
    global lefted
    boool = True
    if rec == 'one':
        if lefted['one'] == 0:
            return False
        for i in range(y, y+1):
            for j in range(x, x+1):
                if i > 9 or j > 9 or maap[i][j] == 0:
                    boool = False
                    return boool
    elif rec == 'two':
        if lefted['two'] == 0:
            return False
        for i in range(y, y+2):
            for j in range(x, x+2):
                if i > 9 or j > 9 or maap[i][j] == 0:
                    boool = False
                    return boool
    elif rec == 'three':
        if lefted['three'] == 0:
            return False
        for i in range(y, y+3):
            for j in range(x, x+3):
                if i > 9 or j > 9 or maap[i][j] == 0:
                    boool = False
                    return boool
    elif rec == 'four':
        if lefted['four'] == 0:
            return False
        for i in range(y, y+4):
            for j in range(x, x+4):
                if i > 9 or j > 9 or maap[i][j] == 0:
                    boool = False
                    return boool
    else:
        if lefted['five'] == 0:
            return False
        for i in range(y, y+5):
            for j in range(x, x+5):
                if i > 9 or j > 9 or maap[i][j] == 0:
                    boool = False
                    return boool
    return boool


def go(y, x, cnt):
    global one, two, three, four, five, results, maap
    if y == 10 :
        results.append(cnt)
        return
    if 0 <= y <=9 and 0<=x<9 and maap[y][x] == 0:
        go(y, x+1, cnt)
    elif 0<=y<=9 and x == 9 and maap[y][x] == 0:
        go(y+1, 0, cnt)
    elif 0<=y<=9 and 0<=x<9 and maap[y][x] == 1:
        boool = False
        for rec in ['one', 'two', 'three', 'four', 'five']:
            if is_possible(maap, y, x, rec):
                boool = True
                #print('y, x, rec : ', y, x, rec)
                make_zeros(maap, y, x, rec)
                lefted[rec] -= 1
                go(y, x+1, cnt+1)
                lefted[rec] += 1
                make_ones(maap, y, x, rec)
        if not boool:
            return
    else:
        boool = False
        for rec in ['one']:
            if is_possible(maap, y, x, rec):
                boool = True
                make_zeros(maap, y, x, rec)
                lefted[rec] -= 1
                go(y+1, 0, cnt + 1)
                lefted[rec] += 1
                make_ones(maap, y, x, rec)
        if not boool:
            return

maap = []

for _ in range(10):
    temp = [int(char) for char in input().split()]
    maap.append(temp)

lefted = {'one':5, 'two':5, 'three':5, 'four':5, 'five':5}
results = []
go(0, 0, 0)
results.sort()


if not results:
    print('-1')
else:
    print(results[0])
