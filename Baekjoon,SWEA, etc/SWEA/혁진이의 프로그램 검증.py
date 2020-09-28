from collections import deque


def inspect(maap, visited):
    queue = deque([[0, 0, 'R', 0]])
    while queue:
        cy, cx, dir, mem = queue.popleft()
        if (dir,mem) in visited[cy][cx]:
            continue
        else:
            visited[cy][cx].append((dir, mem))
        oper = maap[cy][cx]
        if oper == '<':
            dir = 'L'
        elif oper == '>':
            dir = 'R'
        elif oper == '^':
            dir = 'U'
        elif oper == 'v':
            dir = 'D'
        elif oper == '_':
            if mem == 0:
                dir = 'R'
            else:
                dir = 'L'
        elif oper == '|':
            if mem == 0:
                dir = 'D'
            else:
                dir = 'U'
        elif oper == '?':
            queue.append([(cy+1)%H, cx, 'U', mem])
            queue.append([(cy-1)%H, cx, 'D', mem])
            queue.append([cy, (cx+1)%W, 'R', mem])
            queue.append([cy, (cx-1)%W, 'L', mem])
            continue
        elif oper == '.':
            pass
        elif oper == '@':
            return True
        elif oper == '+':
            if mem == 15:
                mem = 0
            else:
                mem += 1
        elif oper == '-':
            if mem == 0:
                mem = 15
            else:
                mem -= 1
        else:  # 0<= <=9
            mem = int(oper)
        if dir == 'R':
            ny, nx = cy, (cx + 1) % W
        elif dir == 'L':
            ny, nx = cy, (cx - 1) % W
        elif dir == 'U':
            ny, nx = (cy - 1) % H, cx
        else:
            ny, nx = (cy + 1) % H, cx
        queue.append([ny, nx, dir, mem])
    return False


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    maap = []
    for _ in range(H):
        temp = input()
        maap.append(temp)
    visited = [[[] for _ in range(W)] for __ in range(H)]
    if inspect(maap, visited):
        print('#{} Yes'.format(tc))
    else:
        print('#{} NO'.format(tc))
