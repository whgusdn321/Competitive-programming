from copy import deepcopy
"""
생각해야 할 것이 많은 문제.
"""


def go(dir, ry, rx, by, bx, depth, maap):
    global results, oy, ox
    if depth == 11:
        return
    owent = []
    if dir == 'up':
        if ry <= by: #
            while maap[ry-1][rx] == '.' or maap[ry-1][rx] == 'O': #
                maap[ry][rx] = '.'
                ry -= 1 #
                if maap[ry][rx] != 'O':
                    maap[ry][rx] = 'R'
                else:
                    owent.append('R')
                    break
            while maap[by-1][bx] == '.' or maap[by-1][bx] == 'O': #
                maap[by][bx] = '.'
                by -= 1#
                if maap[by][bx] != 'O':
                    maap[by][bx] = 'B'
                else:
                    owent.append('B')
                    break
            if 'B' in owent:
                return
            elif 'R' in owent:
                results.append(depth)
                return
            else:
                if (maap[ry][rx-1] == '.' or maap[ry][rx-1] == 'O' ) or\
                        (maap[by][bx-1] == '.' or maap[by][bx-1] == 'O'):
                    go('left', ry, rx, by, bx, depth+1, deepcopy(maap))
                if (maap[ry][rx+1] == '.' or maap[ry][rx+1] == 'O') or\
                        (maap[by][bx+1] == '.' or maap[by][bx+1] == 'O'):
                    go('right', ry, rx, by, bx, depth+1, deepcopy(maap))

        else:
            while maap[by-1][bx] == '.' or maap[by-1][bx] == 'O':
                maap[by][bx] = '.'
                by -= 1
                if maap[by][bx] != 'O':
                    maap[by][bx] = 'B'
                else:
                    owent.append('B')
                    break
            while maap[ry-1][rx] == '.' or maap[ry-1][rx] == 'O':
                maap[ry][rx] = '.'
                ry -= 1
                if maap[ry][rx] != 'O' :
                    maap[ry][rx] = 'R'
                else:
                    owent.append('R')
                    break
            if 'B' in owent:
                return
            elif 'R' in owent:
                results.append(depth)
                return
            else:
                if (maap[ry][rx-1] == '.' or maap[ry][rx-1] == 'O' ) or \
                        (maap[by][bx-1] == '.' or maap[by][bx-1] == 'O'):
                    go('left', ry, rx, by, bx, depth+1, deepcopy(maap))
                if (maap[ry][rx+1] == '.' or maap[ry][rx+1] == 'O') or \
                        (maap[by][bx+1] == '.' or maap[by][bx+1] == 'O'):
                    go('right', ry, rx, by, bx, depth+1, deepcopy(maap))
    elif dir == 'left':
        if rx <= bx: #
            while maap[ry][rx-1] == '.' or maap[ry][rx-1] == 'O': #
                maap[ry][rx] = '.'
                rx -= 1 #
                if maap[ry][rx] != 'O':
                    maap[ry][rx] = 'R'
                else:
                    owent.append('R')
                    break
            while maap[by][bx-1] == '.' or maap[by][bx-1] == 'O': #
                maap[by][bx] = '.'
                bx -= 1#
                if maap[by][bx] != 'O':
                    maap[by][bx] = 'B'
                else:
                    owent.append('B')
                    break
            if 'B' in owent:
                return
            elif 'R' in owent:
                results.append(depth)
                return
            else:
                if (maap[ry-1][rx] == '.' or maap[ry-1][rx] == 'O' ) or \
                        (maap[by-1][bx] == '.' or maap[by-1][bx] == 'O'):
                    go('up', ry, rx, by, bx, depth+1, deepcopy(maap))
                if (maap[ry+1][rx] == '.' or maap[ry+1][rx] == 'O') or \
                        (maap[by+1][bx] == '.' or maap[by+1][bx] == 'O'):
                    go('down', ry, rx, by, bx, depth+1, deepcopy(maap))
        else:
            while maap[by][bx-1] == '.' or maap[by][bx-1] == 'O': #
                maap[by][bx] = '.'
                bx -= 1#
                if maap[by][bx] != 'O':
                    maap[by][bx] = 'B'
                else:
                    owent.append('B')
                    break
            while maap[ry][rx - 1] == '.' or maap[ry][rx - 1] == 'O':  #
                maap[ry][rx] = '.'
                rx -= 1  #
                if maap[ry][rx] != 'O':
                    maap[ry][rx] = 'R'
                else:
                    owent.append('R')
                    break
            if 'B' in owent:
                return
            elif 'R' in owent:
                results.append(depth)
                return
            else:
                if (maap[ry-1][rx] == '.' or maap[ry-1][rx] == 'O' ) or\
                        (maap[by-1][bx] == '.' or maap[by-1][bx] == 'O'):
                    go('up', ry, rx, by, bx, depth+1, deepcopy(maap))
                if (maap[ry+1][rx] == '.' or maap[ry+1][rx] == 'O') or\
                        (maap[by+1][bx] == '.' or maap[by+1][bx] == 'O'):
                    go('down', ry, rx, by, bx, depth+1, deepcopy(maap))
    elif dir == 'right':
        if rx >= bx: #
            while maap[ry][rx+1] == '.' or maap[ry][rx+1] == 'O': #
                maap[ry][rx] = '.'
                rx += 1 #
                if maap[ry][rx] != 'O':
                    maap[ry][rx] = 'R'
                else:
                    owent.append('R')
                    break
            while maap[by][bx+1] == '.' or maap[by][bx+1] == 'O': #
                maap[by][bx] = '.'
                bx += 1#
                if maap[by][bx] != 'O':
                    maap[by][bx] = 'B'
                else:
                    owent.append('B')
                    break
            if 'B' in owent:
                return
            elif 'R' in owent:
                results.append(depth)
                return
            else:
                if (maap[ry-1][rx] == '.' or maap[ry-1][rx] == 'O' ) or \
                        (maap[by-1][bx] == '.' or maap[by-1][bx] == 'O'):
                    go('up', ry, rx, by, bx, depth+1,  deepcopy(maap))
                if (maap[ry+1][rx] == '.' or maap[ry+1][rx] == 'O') or\
                        (maap[by+1][bx] == '.' or maap[by+1][bx] == 'O'):
                    go('down', ry, rx, by, bx, depth+1, deepcopy(maap))
        else:
            while maap[by][bx+1] == '.' or maap[by][bx+1] == 'O': #
                maap[by][bx] = '.'
                bx += 1#
                if maap[by][bx] != 'O':
                    maap[by][bx] = 'B'
                else:
                    owent.append('B')
                    break
            while maap[ry][rx+1] == '.' or maap[ry][rx+1] == 'O': #
                maap[ry][rx] = '.'
                rx += 1 #
                if maap[ry][rx] != 'O':
                    maap[ry][rx] = 'R'
                else:
                    owent.append('R')
                    break
            if 'B' in owent:
                return
            elif 'R' in owent:
                results.append(depth)
                return
            else:
                if (maap[ry-1][rx] == '.' or maap[ry-1][rx] == 'O' ) or\
                        (maap[by-1][bx] == '.' or maap[by-1][bx] == 'O'):
                    go('up', ry, rx, by, bx, depth+1, deepcopy(maap))
                if (maap[ry+1][rx] == '.' or maap[ry+1][rx] == 'O') or \
                        (maap[by+1][bx] == '.' or maap[by+1][bx] == 'O'):
                    go('down', ry, rx, by, bx, depth+1, deepcopy(maap))
    else:  # dir == down
        if ry >= by: #
            while maap[ry+1][rx] == '.' or maap[ry+1][rx] == 'O': #
                maap[ry][rx] = '.'
                ry += 1 #
                if maap[ry][rx] != 'O' :
                    maap[ry][rx] = 'R'
                else:
                    owent.append('R')
                    break
            while maap[by+1][bx] == '.' or maap[by+1][bx] == 'O': #
                maap[by][bx] = '.'
                by += 1#
                if maap[by][bx] != 'O':
                    maap[by][bx] = 'B'
                else:
                    owent.append('B')
                    break
            if 'B' in owent:
                return
            elif 'R' in owent:
                results.append(depth)
                return
            else:
                if (maap[ry][rx-1] == '.' or maap[ry][rx-1] == 'O' )or\
                        (maap[by][bx-1] == '.' or maap[by][bx-1] == 'O'):
                    go('left', ry, rx, by, bx, depth+1, deepcopy(maap))
                if (maap[ry][rx+1] == '.' or maap[ry][rx+1] == 'O') or\
                        (maap[by][bx+1] == '.' or maap[by][bx+1] == 'O'):
                    go('right', ry, rx, by, bx, depth+1, deepcopy(maap))

        else:
            while maap[by + 1][bx] == '.' or maap[by + 1][bx] == 'O':  #
                maap[by][bx] = '.'
                by += 1  #
                if maap[by][bx] != 'O':
                    maap[by][bx] = 'B'
                else:
                    owent.append('B')
                    break
            while maap[ry + 1][rx] == '.' or maap[ry + 1][rx] == 'O':  #
                maap[ry][rx] = '.'
                ry += 1  #
                if maap[ry][rx] != 'O':
                    maap[ry][rx] = 'R'
                else:
                    owent.append('R')
                    break
            if 'B' in owent:
                return
            elif 'R' in owent:
                results.append(depth)
                return
            else:
                if (maap[ry][rx-1] == '.' or maap[ry][rx-1] == 'O' )or\
                        (maap[by][bx-1] == '.' or maap[by][bx-1] == 'O'):
                    go('left', ry, rx, by, bx, depth+1, deepcopy(maap))
                if (maap[ry][rx+1] == '.' or maap[ry][rx+1] == 'O') or\
                        (maap[by][bx+1] == '.' or maap[by][bx+1] == 'O'):
                    go('right', ry, rx, by, bx, depth+1, deepcopy(maap))



N, M = map(int, input().split())
maap = []
for _ in range(N):
    temp = [char for char in input()]
    maap.append(temp)
ry = None
rx = None
by = None
bx = None
oy = None
ox = None
for i in range(N):
    for j in range(M):
        if maap[i][j] == 'O':
            oy, ox = i, j
        elif maap[i][j] == 'R':
            ry, rx = i, j
        elif maap[i][j] == 'B':
            by, bx = i, j
        else:  # '#'
            pass
#print(oy, ox)
#print(ry, rx)
#print(by, bx)
results = []
if (maap[ry][rx - 1] == '.' or maap[ry][rx - 1] == 'O' ) or \
        (maap[by][bx - 1] == '.' or maap[by][bx - 1] == 'O'):
        go('left', ry, rx, by, bx, 1, deepcopy(maap))
if (maap[ry][rx + 1] == '.' or maap[ry][rx + 1] == 'O') or \
        (maap[by][bx + 1] == '.' or maap[by][bx + 1] == 'O'):
    go('right', ry, rx, by, bx, 1, deepcopy(maap))
if (maap[ry - 1][rx] == '.' or maap[ry - 1][rx] == 'O') or \
        (maap[by - 1][bx] == '.' or maap[by - 1][bx] == 'O'):
    go('up', ry, rx, by, bx, 1, deepcopy(maap))
if (maap[ry + 1][rx] == '.' or maap[ry + 1][rx] == 'O') or \
        (maap[by + 1][bx] == '.' or maap[by + 1][bx] == 'O'):
    go('down', ry, rx, by, bx, 1, deepcopy(maap))
if results :
    print(min(results))
else:
    print(-1)