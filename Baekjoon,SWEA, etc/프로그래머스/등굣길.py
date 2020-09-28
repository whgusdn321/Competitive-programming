def solution(m, n, puddles):
    W, H = m, n
    visited = [[0] * W for _ in range(H)]
    for puddle in puddles:
        visited[puddle[1] - 1][puddle[0] - 1] = -1
    visited[0][0] = 0

    #for column
    j = 0
    for i in range(1, H):
        if visited[i][0] == -1:
            j = i
            break
        else:
            visited[i][0] = 1

    if j != 0:
        for i in range(j, H):
            visited[i][0] = 0

    #for row
    j = 0
    for i in range(1, W):
        if visited[0][i] == -1:
            j = i
            break
        else:
            visited[0][i] = 1
    if j != 0:
        for j in range(j, W):
            visited[0][j] = 0

    for i in range(1, H):
        for j in range(1, W):
            if visited[i][j] == -1:
                visited[i][j] = 0
            else:
                visited[i][j] = visited[i][j-1] + visited[i-1][j]
    # print('visited : ')
    # for _ in range(H):
    #     print(visited[_])
    return (visited[H-1][W-1])%1000000007
print(solution(4, 3, [[2, 2]]))