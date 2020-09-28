import sys
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    temp = [int(a) for a in sys.stdin.readline().split()]
    arr.append(temp)
visited = [False] * N


def go(start, before, goal):
    visited = [False]*N
    if start == goal:
        return True
    if before:
        visited[before] = True

    boool = False
    for i in range(N):
        if arr[start][i] == 1 and not visited[i]:
            boool |= go(i, start, goal)
    return boool


b = [[-1]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        visited = [False] * N
        if go(i, None, j):
            b[i][j] = 1
        else:
            b[i][j] = 0
#print(go(1, None, 1))
for _ in range(N):
    print('b : ', b[_])