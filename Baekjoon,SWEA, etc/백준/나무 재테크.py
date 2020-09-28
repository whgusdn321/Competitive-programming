def spring(alive, dead, left_nutri):
    global N
    for i in range(N):
        for j in range(N):
            if alive[i][j]:
                alive[i][j].sort()
                trees = alive[i][j]
                o = 0
                while o < len(trees) and left_nutri[i][j] >= trees[o]:
                    left_nutri[i][j] -= trees[o]
                    trees[o] += 1
                    o += 1
                for _ in range(len(trees)-o):
                    t = trees.pop()
                    dead[i][j].append(t)


def summer(dead, left_nutri):
    global N
    for i in range(N):
        for j in range(N):
            if dead[i][j]:
                while dead[i][j]:
                    e = dead[i][j].pop()
                    left_nutri[i][j] += e//2


def fall(alive):
    global N
    for i in range(N):
        for j in range(N):
            adj = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            for tree in alive[i][j]:
                if tree % 5 == 0:
                    for dy, dx in adj:
                        if 0<=dy<N and 0<=dx<N:
                            alive[dy][dx].append(1)


def winter(left_nutri, A):
    global N
    for i in range(N):
        for j in range(N):
            left_nutri[i][j] += A[i][j]


N, M, K = map(int, input().split())
A = []
alive = [[[] for _ in range(N)] for __ in range(N)]
dead = [[[] for _ in range(N)] for ___ in range(N)]
left_nutri = [[5]*N for _ in range(N)]

for _ in range(N):
    temp = [int(char) for char in input().split()]
    A.append(temp)

for _ in range(M):
    y, x, z = map(int, input().split())
    y -= 1
    x -= 1
    alive[y][x].append(z)


for year in range(K):
    spring(alive, dead, left_nutri)
    summer(dead, left_nutri)
    fall(alive)
    winter(left_nutri, A)

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(alive[i][j])
print(cnt)