from collections import deque
#colum = {'1':7, '2':6, '3':5, '4':4, '5':3, '6':2, '7':1, '8':0}
#row = {'A':0, 'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H':7,}

#rev_col = {7:'1', 6:'2', 5:'3', 4:'4',3:'5',2:'6',1:'7',0:'8'}
#rev_row = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}

king, stone, N = input().split()
N = int(N)
opers = []
for _ in range(N):
    opers.append(input())
opers = deque(opers)
maap = [[0] * 8 for _ in range(8)]

kingcol = int(king[1])-1
kingrow = ord(king[0])-65

stonecol = int(stone[1])-1
stonerow = ord(stone[0])-65

maap[kingcol][kingrow] = 'king'
maap[stonecol][stonerow] = 'stone'


def dydx(oper):
    if oper == 'R':
        return (0, 1)
    elif oper == 'L':
        return (0, -1)
    elif oper == 'B':
        return (-1, 0)
    elif oper == 'T':
        return (1, 0)
    elif oper == 'RT':
        return (1, 1)
    elif oper == 'LT':
        return (1, -1)
    elif oper == 'RB':
        return (-1, 1)
    else:
        return (-1, -1)


kcol, krow = kingcol, kingrow
scol, srow = stonecol, stonerow


while opers:
    oper = opers.popleft()
    dy, dx = dydx(oper)
    toy = kcol + dy
    tox = krow + dx
    if not ((0<=toy<8) and (0<=tox<8)):
        continue
    if maap[toy][tox] == 'stone':
        tosy = scol + dy
        tosx = srow + dx
        if not ((0<=tosy<8) and (0<=tosx<8)):
            continue
        else:
            maap[kcol][krow] = 0
            maap[scol][srow] = 0
            kcol, krow = toy, tox
            scol, srow = tosy, tosx
            maap[kcol][krow] = 'king'
            maap[scol][srow] = 'stone'
    else:
        maap[kcol][krow] = 0
        kcol, krow = toy, tox
        maap[kcol][krow] = 'king'

fkcol, fkrow = None, None

fscol, fsrow = None, None
for y in range(8):
    for x in range(8):
        if maap[y][x] == 'king':
            fkcol = y
            fkrow = x
        if maap[y][x] == 'stone':
            fscol = y
            fsrow = x

print('{}{}'.format(chr(fkrow+65), fkcol+1))
print('{}{}'.format(chr(fsrow+65), fscol+1))
