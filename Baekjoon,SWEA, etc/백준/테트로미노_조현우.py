import sys
sys.setrecursionlimit(1000000000)
read = lambda :sys.stdin.readline().rstrip()

H, W = map(int, read().split())
maap = []
visited= []
for _ in range(H):
    temp = [int(a) for a in read().split()]
    maap.append(temp)
    visited.append([False]*W)
sums = []


def dfs(y, x, sum, cnt):
    global maap, visited, sums
    if cnt == 4:
        sums.append(sum)
        return
    adjacent = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adjacent:
        if 0<=dy<H and 0<=dx<W:
            if not visited[dy][dx]:
                visited[dy][dx] = True
                dfs(dy, dx, sum+maap[dy][dx], cnt+1)
                visited[dy][dx] = False


for i in range(H):
    for j in range(W):
        # visited = [[False]*W for _ in range(H)]
        visited[i][j] = True
        sum = maap[i][j]
        cnt = 1
        dfs(i, j, sum, cnt)
        visited[i][j] = False
        if 0<=i-1<H and 0<=i+1<H and 0<= j+1<W:
            sums.append(maap[i][j] + maap[i-1][j] + maap[i][j+1]+maap[i+1][j])
        if 0<=i-1<H and 0<=j-1<W and 0<=j+1<W:
            sums.append(maap[i][j]+ maap[i-1][j]+maap[i][j+1]+maap[i][j-1])
        if 0<=i-1<H and 0<=i+1<H and 0<=j-1<W:
            sums.append(maap[i][j] + maap[i-1][j] + maap[i+1][j] + maap[i][j-1])
        if 0<=i+1<H and 0<=j-1<W and 0<=j+1<W:
            sums.append(maap[i][j] + maap[i][j+1]+maap[i+1][j]+maap[i][j-1])

print(max(sums))