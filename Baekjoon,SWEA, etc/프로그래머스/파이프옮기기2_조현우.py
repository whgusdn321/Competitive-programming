import sys
read = lambda :sys.stdin.readline().rstrip()

N = int(read())

maap =[]
for _ in range(N):
    temp = [int(a) for a in read().split()]
    maap.append(temp)

visited = [[[0,0,0] for _ in range(N-1)] for _ in range(N)]

for i in range(0, N-1):
    if maap[0][i+1] == 1:
        break
    visited[0][i][0] = 1

for i in range(1, N):
    for j in range(1, N-1):
        if maap[i][j+1] == 1:
            continue
        else:
            if maap[i][j] != 1:
                visited[i][j][0] = visited[i][j-1][0] + visited[i][j-1][2]
            else:
                visited[i][j][0] = 0
            if maap[i-1][j+1] != 1:
                visited[i][j][1] = visited[i-1][j][1] + visited[i-1][j][2]
            else:
                visited[i][j][1] = 0
            if maap[i-1][j+1] != 1 and maap[i-1][j] != 1 and maap[i][j] != 1:
                visited[i][j][2] = visited[i-1][j-1][0] + visited[i-1][j-1][1] + visited[i-1][j-1][2]
            else:
                visited[i][j][2] =0


print(sum(visited[N-1][N-2]))
