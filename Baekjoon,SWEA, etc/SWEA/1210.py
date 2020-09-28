def go(maap, Xy, Xx):
    sy, sx, dirc = Xy, Xx, 'N'

    while True:
        if sy == 0:
            return sx

        if dirc == 'E':
            if maap[sy-1][sx] == 1:
                dirc = 'N'
                sy -= 1
                continue
            else:
                sx += 1
                continue

        elif dirc == 'W':
            if maap[sy-1][sx] == 1:
                dirc = 'N'
                sy -= 1
                continue
            else:
                sx -= 1
                continue

        else:  # dirc == 'N'
            if sx + 1 < 100 and maap[sy][sx+1] == 1:
                sx += 1
                dirc = 'E'
                continue
            elif sx - 1 >= 0 and maap[sy][sx-1] == 1:
                dirc = 'W'
                sx -= 1
                continue
            else:
                sy -= 1
                continue



T = 10
for tc in range(1, T+1):
    __ = input()
    maap = []
    for _ in range(100):
        temp = [int(a) for a in input().split()]
        maap.append(temp)

    # find Xy, Xx
    Xy, Xx = 0, 0
    for i in range(100):
        for j in range(100):
            if maap[i][j] == 2:
                Xy = i
                Xx = j
                break

    j = go(maap, Xy, Xx)
    print('#{} {}'.format(tc, j))

