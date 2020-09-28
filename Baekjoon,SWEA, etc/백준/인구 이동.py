import sys
sys.setrecursionlimit(1000000000)
def go(y, x, stakk, summ):
    global visited, maap, N, L, R
    visited[y][x] = True
    stakk.append((y, x))
    summ += maap[y][x]

    adj = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adj:
        if 0 <= dy < N and 0 <= dx < N and not visited[dy][dx]:
            if L <= abs(maap[y][x] - maap[dy][dx]) <= R:
                stakk, summ = go(dy, dx, stakk, summ)

    return stakk, summ


N, L, R = map(int, input().split())
maap = []

for _ in range(N):
    temp = [int(char) for char in input().split()]
    maap.append(temp)

boool = True
cnt = 0

while boool:
    boool = False
    visited = [[False] *N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                stakk, summ = go(i, j, [], 0)
                if len(stakk) > 1:
                    boool = True
                    for _y, _x in stakk:
                        maap[_y][_x] = summ//len(stakk)
    if boool:
        cnt += 1
    else:
        break
print(cnt)
