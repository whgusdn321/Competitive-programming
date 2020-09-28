def inspect(y, x, k):
    global maap, M
    money = k**2 + (k-1)**2
    houses = []
    for i in range((y-k+1), (y+k)):
        for j in range((x-k+1), (x+k)):
            if 0 <= i < N and 0 <= j < N and abs(i-y) + abs(j-x) <= k-1:
                if maap[i][j] == 1:
                    houses.append((i,j))
    if len(houses)*M - money >= 0:
        return houses
    else:
        return None


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maap = []
    for _ in range(N):
        temp =[int(a) for a in input().split()]
        maap.append(temp)
    results = []
    for k in range(N+2, 0, -1):
        boool = False
        for i in range(N):
            for j in range(N):
                houses = inspect(i, j, k)
                if houses:
                    results.append(len(houses))
                    boool = True
        if boool:
            break
    print('#{} {}'.format(tc, max(results)))
