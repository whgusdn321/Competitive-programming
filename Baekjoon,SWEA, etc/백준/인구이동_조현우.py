import sys
sys.setrecursionlimit(1000000000)
N, L, R = map(int, sys.stdin.readline().split())
maap = []
for _ in range(N):
    temp = [int(a) for a in sys.stdin.readline().split()]
    maap.append(temp)


def dfs(y, x, stack):
    global visited, sums
    visited[y][x] = True
    stack.append((y, x))
    sums += maap[y][x]

    adjacent = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adjacent:
        if 0 <= dy < N and 0 <= dx < N and not visited[dy][dx]:
            if L <= abs(maap[y][x] - maap[dy][dx]) <= R:
                dfs(dy, dx, stack)
    return stack


k = 0
while True:
    visited = [[False] * N for _ in range(N)]
    boool = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                sums = 0
                stack = dfs(i, j, [])
                if len(stack) > 1:
                    boool = True
                    for dy, dx in stack:
                        maap[dy][dx] = sums // len(stack)

    if k>2000:
        break
    if not boool:
        break
    else:
        k += 1

print(k)

