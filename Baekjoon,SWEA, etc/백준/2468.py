import sys
sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
maap = []

for _ in range(N):
    temp = [int(a) for a in sys.stdin.readline().split()]
    maap.append(temp)


def go(y, x, visited, k):
    if maap[y][x]<=k:
        return False
    elif not visited[y][x]:
        visited[y][x] = True
        adjacent = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
        for dy, dx in adjacent:
            if 0<=dy<N and 0<=dx<N and not visited[dy][dx]:
                if maap[dy][dx]>k:
                    go(dy, dx, visited, k)
        return True
    else:
        return False

kk = []
for k in range(0, 101):
    visited = [[False]*N for __ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            boool = go(i, j, visited, k)
            if boool:
                cnt += 1
    kk.append(cnt)
print(max(kk))