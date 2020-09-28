T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(char) for char in input().split()]
        maap.append(temp)

    results = []
    for y in range(N):
        for x in range(N):
            for i in range(1, N):
                for j in range(1, N):
                    if x-j >= 0 and x+i < N and y + i + j < N:
                        stakk = []
                        boool = True
                        dy, dx = (1, 1)
                        sy, sx = (y, x)
                        for _ in range(i):
                            sy, sx = sy + dy, sx + dx
                            if maap[sy][sx] not in stakk:
                                stakk.append(maap[sy][sx])
                            else:
                                boool = False
                        if not boool:
                            continue

                        dy, dx = (1, -1)
                        for _ in range(j):
                            sy, sx = sy + dy, sx + dx
                            if maap[sy][sx] not in stakk:
                                stakk.append(maap[sy][sx])
                            else:
                                boool = False
                        if not boool:
                            continue

                        dy, dx = (-1, -1)
                        for _ in range(i):
                            sy, sx = sy + dy, sx + dx
                            if maap[sy][sx] not in stakk:
                                stakk.append(maap[sy][sx])
                            else:
                                boool = False
                        if not boool:
                            continue

                        dy, dx = (-1, 1)
                        for _ in range(j):
                            sy, sx = sy + dy, sx + dx
                            if maap[sy][sx] not in stakk:
                                stakk.append(maap[sy][sx])
                            else:
                                boool = False
                        if not boool:
                            continue
                        results.append(len(stakk))
    if results:
        print('#{} {}'.format(tc, max(results)))
    else:
        print('#{} {}'.format(tc, -1))




