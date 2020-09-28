def move(y, x, dir):
    if dir == 'right':
        return y, x+1
    elif dir == 'left':
        return y, x-1
    elif dir == 'down':
        return y+1, x
    else:
        return y-1, x


N = int(input())
maap = [[0]*N for _ in range(N)]
K = int(input())
for k in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    maap[a][b] = 'apple'

L = int(input())
dTime = []
ddir = []
for l in range(L):
    x, C = input().split()
    x = int(x)
    dTime.append(x)
    ddir.append(C)

visited = [[0]*N for _ in range(N)]
ty, tx, tdir = 0, 0, 'right'
hy, hx, hdir = 0, 0, 'right'
visited[0][0] = 'right'
time = 0

while True:
    time += 1
    if hdir == 'right':
        if 0<=hx+1<N:
            hy, hx = move(hy, hx, hdir)
            if visited[hy][hx] != 0:
                break
            else:
                visited[hy][hx] = hdir
                if maap[hy][hx] == 'apple':
                    maap[hy][hx] = 0
                else:
                    visited[ty][tx] = 0
                    ty, tx = move(ty, tx, tdir)
                    tdir = visited[ty][tx]
        else:
            break
    elif hdir == 'left':
        if 0<= hx-1<N:
            hy, hx = move(hy, hx, hdir)
            if visited[hy][hx] != 0:
                break
            else:
                visited[hy][hx] = hdir
                if maap[hy][hx] == 'apple':
                    maap[hy][hx] = 0
                else:
                    visited[ty][tx] = 0
                    ty, tx = move(ty, tx, tdir)
                    tdir = visited[ty][tx]
        else:
            break
    elif hdir == 'up':
        if 0<= hy-1 < N:
            hy, hx = move(hy, hx, hdir)
            if visited[hy][hx] != 0:
                break
            else:
                visited[hy][hx] = hdir
                if maap[hy][hx] == 'apple':
                    maap[hy][hx] = 0
                else:
                    visited[ty][tx] = 0
                    ty, tx = move(ty, tx, tdir)
                    tdir = visited[ty][tx]
        else:
            break
    else: # hdir == 'down'
        if 0 <= hy+1 < N:
            hy, hx = move(hy, hx, hdir)
            if visited[hy][hx] != 0:
                break
            else:
                visited[hy][hx] = hdir
                if maap[hy][hx] == 'apple':
                    maap[hy][hx] = 0
                else:
                    visited[ty][tx] = 0
                    ty, tx = move(ty, tx, tdir)
                    tdir = visited[ty][tx]
        else:
            break

    if time in dTime:
        c = ddir[dTime.index(time)]
        if c == 'D':  # 오른쪽으로 90도
            if hdir == 'left':
                hdir = 'up'
            elif hdir == 'up':
                hdir = 'right'
            elif hdir == 'right':
                hdir = 'down'
            else:
                hdir = 'left'
        else:
            if hdir == 'up':
                hdir = 'left'
            elif hdir == 'left':
                hdir = 'down'
            elif hdir == 'down':
                hdir = 'right'
            else:
                hdir = 'up'
        visited[hy][hx] = hdir
        if hy == ty and hx == tx:
            tdir = hdir

print(time)
# print('maap : ')
# for _ in range(N):
#     print(maap[_])
# print('visited : ')
# for _ in range(N):
#     print(visited[_])




