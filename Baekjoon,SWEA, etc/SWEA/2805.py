T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(a) for a in input()]
        maap.append(temp)

    x = N//2
    sum = 0
    for y in range(0, N//2+1, 1):
        sum += maap[y][x]
        for dx in range(1, y+1):
            sum += maap[y][x+dx]
            sum += maap[y][x-dx]
    for y in range(N//2+1, N, 1):
        sum += maap[y][x]
        for dx in range(1, N-y):
            sum += maap[y][x+dx]
            sum += maap[y][x-dx]
    print('#{} {}'.format(tc, sum))