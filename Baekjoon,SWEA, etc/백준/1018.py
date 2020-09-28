import sys
read = lambda: sys.stdin.readline().rstrip()

N, M = map(int, read().split())
maap = [read() for _ in range(N)]

cnts = []

for toplefty in range(N-7):
    for topleftx in range(M-7):
        cnt = 0
        before = maap[toplefty][topleftx]
        for i in range(toplefty, toplefty+8):
            for j in range(topleftx, topleftx+8):
                if i == toplefty and j == topleftx:
                    continue
                if maap[i][j] == before:
                    cnt += 1
                    if before == 'B':
                        before = 'W'
                    else:
                        before = 'B'
                else: #when different
                    before = maap[i][j]

                if j == topleftx+7:
                    if before == 'W':
                        before = 'B'
                    else:
                        before = 'W'
        cnts.append(min(cnt, 64-cnt))

print(min(cnts))