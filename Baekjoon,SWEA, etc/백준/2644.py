import sys
read = lambda :sys.stdin.readline().rstrip()

N = int(read())
n1, n2 = map(int, read().split())
M = int(read())
maap = [-1] * (N+1)

for _ in range(M):
    parent, child = map(int, read().split())
    maap[child] = parent


cur = [[0]] + [[a] for a in range(1, N+1)]
move = [[0] for _ in range(N+1)]


def go(cur, move, maap):
    for i in range(1, N+1):
        if maap[cur[i][-1]] != -1:
            cur[i].append(maap[cur[i][-1]])
            move[i].append(move[i][-1]+1)


while cur[n1][-1] != cur[n2][-1]:
    go(cur, move, maap)
    if maap[cur[n1][-1]] == -1 and maap[cur[n2][-1]] ==-1 and cur[n1][-1]!= cur[n2][-1]:
        print(-1)
        sys.exit()


for i in range(len(cur[n1])):
    for j in range(len(cur[n2])):
        if cur[n1][i] == cur[n2][j]:
            print(move[n1][i]+move[n2][j])
            sys.exit()
