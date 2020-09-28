N = int(input())


def nqueen(i, j, parents):
    global N, cnt
    promising = True

    for pi, pj in parents:
        if j == pj or abs(i - pi) == abs(j - pj):
            promising = False
            break
    if promising:
        parents.append((i, j))
        if i == N - 1:
            cnt += 1
            parents.pop()
            return
        else:
            for child in range(0, N):
                nqueen(i+1, child, parents)
            parents.pop()

cnt = 0
for i in range(N):
    nqueen(0, i, [])
print(cnt)