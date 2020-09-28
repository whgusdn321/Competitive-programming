# def go(dir, y, x):
#     global visited, N, maap
#
#     if 0 <= y < N and 0 <= x < N:
#         if dir == 'traj':
#             if maap[y][x] == 0 and maap[y-1][x] == 0 and maap[y][x-1] == 0:
#                 visited[y][x] += 1
#                 go('garo', y, x+1)
#                 go('sero', y+1, x)
#                 go('traj', y+1, x+1)
#         elif dir == 'garo':
#             if maap[y][x] == 0:
#                 visited[y][x] += 1
#                 go('garo', y, x + 1)
#                 go('traj', y + 1, x + 1)
#         else:
#             if maap[y][x] == 0:
#                 visited[y][x] += 1
#                 go('sero', y+1, x)
#                 go('traj', y+1, x+1)
#
#
#

N = int(input())
maap = []
for _ in range(N):
    temp = [int(a) for a in input().split()]
    maap.append(temp)
visited = [[[0, 0, 0] for _ in range(N)] for __ in range(N)]
visited[0][1][0] = 1

for i in range(N):
    for j in range(N):
        #가로
        if j+1 < N and maap[i][j+1] == 0:
            visited[i][j+1][0] += visited[i][j][0]
        if i+1 < N and j+1 < N and maap[i+1][j+1] == 0 and maap[i][j+1] == 0 and maap[i+1][j]==0:
            visited[i+1][j+1][2] += visited[i][j][0]
        #세로
        if i+1<N and maap[i+1][j] == 0:
            visited[i+1][j][1] += visited[i][j][1]
        if i+1 < N and j+1 < N and maap[i+1][j+1] == 0 and maap[i][j+1] == 0 and maap[i+1][j]==0:
            visited[i+1][j+1][2] += visited[i][j][1]
        #대각방향
        if j+1<N and maap[i][j+1] == 0:
            visited[i][j+1][0] += visited[i][j][2]
        if i+1<N and maap[i+1][j] == 0:
            visited[i+1][j][1] += visited[i][j][2]
        if i+1<N and j+1<N and maap[i+1][j+1] == 0 and maap[i][j+1] == 0 and maap[i+1][j]==0:
            visited[i+1][j + 1][2] += visited[i][j][2]


print(sum(visited[N-1][N-1]))















