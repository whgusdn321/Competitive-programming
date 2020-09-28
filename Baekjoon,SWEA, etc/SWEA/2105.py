def inspect(maap):
    global N, results

    for y in range(N):
        for x in range(N):
            for i in range(1, N):
                for j in range(1, N):

                    boool = True
                    a, b = i, j

                    firsty, firstx = y, x
                    twoy, twox = firsty + a, firstx + a
                    threey, threex = twoy + b, twox - b
                    foury, fourx = threey - a, threex - a

                    if 0 <= twoy < N and 0 <= twox < N and 0 <= threey < N and 0 <= threex < N and 0 <= foury < N and 0 <= fourx < N:
                        visited = []
                        cy, cx = y, x
                        dy, dx = (1, 1)
                        for _ in range(a):
                            cy, cx = cy + dy, cx + dx
                            if maap[cy][cx] not in visited:
                                visited.append(maap[cy][cx])
                            else:
                                boool = False
                                break
                        if boool:
                            dy, dx = (1, -1)
                            for _ in range(b):
                                cy, cx = cy + dy, cx + dx
                                if maap[cy][cx] not in visited:
                                    visited.append(maap[cy][cx])
                                else:
                                    boool = False
                                    break
                        if boool:
                            dy, dx = (-1, -1)
                            for _ in range(a):
                                cy, cx = cy + dy, cx + dx
                                if maap[cy][cx] not in visited:
                                    visited.append(maap[cy][cx])
                                else:
                                    boool = False
                                    break
                        if boool:
                            dy, dx = (-1, 1)
                            for _ in range(b):
                                cy, cx = cy + dy, cx + dx
                                if maap[cy][cx] not in visited:
                                    visited.append(maap[cy][cx])
                                else:
                                    boool = False
                                    break
                        if boool:
                            results.append(len(visited))




test_cases = int(input())
for test_case in range(1, test_cases + 1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(a) for a in input().split()]
        maap.append(temp)

    results = []
    inspect(maap)
    if results:
        print('#{} {}'.format(test_case , max(results)))
    else:
        print('#{} {}'.format(test_case, -1))