from copy import deepcopy


def find_max(maap):
    global N
    _max = 0
    for i in range(N):
        for j in range(N):
            if maap[i][j] > _max:
                _max = maap[i][j]
    return _max


def move(maap, dir, depth):
    global N, results
    visited = [[False] * N for _ in range(N)]
    if depth == 6:
        max_item = find_max(maap)
        results.append(max_item)
        return

    if dir == 'up':
        for j in range(0, N): #
            for i in range(0, N): #
                if maap[i][j] != 0:
                    ii = i-1 #
                    while ii >= 0 and maap[ii][j] == 0:#
                        ii -= 1#
                    if ii >= 0 and maap[ii][j] == maap[i][j] and not visited[ii][j]:#
                        maap[ii][j] += maap[i][j]
                        maap[i][j] = 0
                        visited[ii][j] = True
                    else:
                        maap[ii+1][j] = maap[i][j]
                        if ii + 1 != i:
                            maap[i][j] = 0
    elif dir == 'down':
        for j in range(0, N):
            for i in range(N-1, -1, -1):
                if maap[i][j] != 0:
                    ii = i + 1
                    while ii < N and maap[ii][j] == 0:
                        ii += 1
                    if ii < N and maap[ii][j] == maap[i][j] and not visited[ii][j]:
                        maap[ii][j] += maap[i][j]
                        maap[i][j] = 0
                        visited[ii][j] = True
                    else:
                        maap[ii-1][j] = maap[i][j]
                        if ii - 1 != i:
                            maap[i][j] = 0

    elif dir == 'right':
        for i in range(0, N):
            for j in range(N-1, -1, -1):
                if maap[i][j] != 0:
                    jj = j+1
                    while jj < N and maap[i][jj] == 0:
                        jj += 1
                    if jj < N and maap[i][jj] == maap[i][j] and not visited[i][jj]:
                        maap[i][jj] += maap[i][j]
                        maap[i][j] = 0
                        visited[i][jj] = True
                    else:
                        maap[i][jj-1] = maap[i][j]
                        if jj -1 != j:
                            maap[i][j] = 0
    else:  # left
        for i in range(0, N):
            for j in range(0, N):
                if maap[i][j] != 0:
                    jj = j - 1
                    while jj >= 0 and maap[i][jj] == 0:
                        jj -= 1
                    if jj >=0 and maap[i][jj] == maap[i][j] and not visited[i][jj]:
                        maap[i][jj] += maap[i][j]
                        maap[i][j] = 0
                        visited[i][jj] = True
                    else:
                        maap[i][jj + 1] = maap[i][j]
                        if jj + 1 != j:
                            maap[i][j] = 0

    move(deepcopy(maap), 'up', depth + 1)
    move(deepcopy(maap), 'down', depth + 1)
    move(deepcopy(maap), 'left', depth + 1)
    move(deepcopy(maap), 'right', depth + 1)


N = int(input())
maap = []
for _ in range(N):
    temp = [int(char) for char in input().split()]
    maap.append(temp)
results = []

max_item = find_max(maap)
#results.append(max_item)

move(deepcopy(maap), 'up', 1)
move(deepcopy(maap), 'down', 1)
move(deepcopy(maap), 'left', 1)
move(deepcopy(maap), 'right', 1)
print(max(results))


