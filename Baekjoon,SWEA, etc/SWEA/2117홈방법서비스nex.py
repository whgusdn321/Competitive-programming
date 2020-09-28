def inspect(maap, i, j, k):
    global M, N
    cost = -(k**2 + (k-1)**2)
    houses = 0
    for y in range(i-k, i+k+1):
        for x in range(j-k, j+k+1):
            if abs(y-i) + abs(j-x) < k:
                if 0<=y<N and 0<=x<N and maap[y][x] == 1:
                    houses += 1
    cost += houses * M
    if cost >= 0:
        return houses
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maap = []
    for _ in range(N):
        temp =[int(a) for a in input().split()]
        maap.append(temp)

    results = []
    for k in range(2*N+1, 0, -1):
        boool = False
        for i in range(N):
            for j in range(N):
                res = inspect(maap, i, j, k)
                if res != 0:
                    results.append(res)
                    boool = True
        if boool:
            break
    print('#{} {}'.format(tc, max(results)))