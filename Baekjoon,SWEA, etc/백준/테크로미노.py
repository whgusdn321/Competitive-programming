def go(i, j, summ, depth):
    global results, maap, visited

    if depth == 4:
        results.append(summ)
        return

    adjacents = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
    for dy, dx in adjacents:
        if 0 <= dy < H and 0 <= dx < W and not visited[dy][dx]:
            visited[dy][dx] = True
            go(dy, dx, summ+maap[dy][dx], depth+1)
            visited[dy][dx] = False


def middlefinger(i, j):
    global maap, results
    a = maap[i][j]
    # ㅗ
    if i-1>=0 and 0<=j-1 and j+1<W:
        a += maap[i-1][j]
        a += maap[i][j-1]
        a += maap[i][j+1]
        results.append(a)
    a = maap[i][j]
    # ㅓ
    if i-1 >=0 and 0<=j-1 and i+1 <H:
        a += maap[i-1][j]
        a += maap[i][j-1]
        a += maap[i+1][j]
        results.append(a)
    a = maap[i][j]
    #ㅏ
    if i-1 >= 0 and i+1<H and j+1<W:
        a += maap[i][j+1]
        a += maap[i-1][j]
        a += maap[i+1][j]
        results.append(a)
    a = maap[i][j]
    #ㅜ
    if i+1<H and j-1>=0 and j+1 < W:
        a += maap[i+1][j]
        a += maap[i][j-1]
        a += maap[i][j+1]
        results.append(a)


H, W = map(int, input().split())
maap = []
visited = [[False]*W for _ in range(H)]
for _ in range(H):
    temp = [int(a) for a in input().split()]
    maap.append(temp)
results = []
for i in range(H):
    for j in range(W):
        visited[i][j] = True
        go(i, j, maap[i][j], 1)
        visited[i][j] = False
        middlefinger(i, j)
print(max(results))

