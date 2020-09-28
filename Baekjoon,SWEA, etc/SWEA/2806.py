#N-queen 문제
def isPromising(visited, depth, i):
    boool = True
    # 행검사
    for y in range(depth - 1, -1, -1):
        if visited[y][i] == True:
            boool = False
            break
    # 대각선 검사
    dy, dx = (-1, -1)
    cy, cx = depth, i
    while 0 <= cy + dy < N and 0 <= cx + dx < N:
        cy += dy
        cx += dx
        if visited[cy][cx]:
            boool = False
            break

    dy, dx = (-1, 1)
    cy, cx = depth, i
    while 0 <= cy + dy < N and 0 <= cx + dx < N:
        cy += dy
        cx += dx
        if visited[cy][cx]:
            boool = False
            break
    return boool


def nqueen(depth, visited):
    global N, cnt
    for i in range(N):
        visited[depth][i] = True
        if isPromising(visited, depth, i):
            if depth == N-1:
                cnt += 1
                return
            else:
                nqueen(depth+1, visited)
        visited[depth][i] = False





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    nqueen(0, visited)
    print('#{} {}'.format(tc,cnt))