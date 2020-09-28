import sys

sys.setrecursionlimit(1000000000)
vec = []


def dfs(y, x, land, terr, visited, t, height):
    visited[y][x] = True
    terr[y][x] = t
    n = len(land)
    for ny, nx in ((y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1)):
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            if abs(land[y][x] - land[ny][nx]) <= height:
                dfs(ny, nx, land, terr, visited, t, height)
            else:
                vec.append((y, x, ny, nx, abs(land[y][x] - land[ny][nx])))


def solution(land, height):
    answer = 0
    m = land
    n = len(land)
    visited = [[False for _ in range(n)] for __ in range(n)]
    terr = [[-1 for _ in range(n)] for __ in range(n)]
    t = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                t += 1
                dfs(i, j, land, terr, visited, t, height)
    # print("vec is : ", vec)
    # for ter in terr:
    #     print(ter)
    vec.sort(key=lambda x: x[4])
    set_list = [set([j]) for j in range(1, t + 1)]
    cnt = 0
    for y1, x1, y2, x2, diff in vec:
        if terr[y1][x1] == terr[y2][x2]:
            continue
        else:
            # find set1, set2 and if they are different set, union them
            idx1 = None
            idx2 = None
            for i in range(len(set_list)):
                if terr[y1][x1] in set_list[i]:
                    idx1 = i
                if terr[y2][x2] in set_list[i]:
                    idx2 = i
                    if idx1 != idx2:


r