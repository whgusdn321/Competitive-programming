def go(y, x, summ):
    global visited, maap, maaap, N
    adjacent = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adjacent:
        if 0 <= dy < N and 0 <= dx < N and not visited[dy][dx]:
            visited[dy][dx] = True
            summ += maaap[dy][dx]
            maap[dy][dx].append(summ)
            go(dy, dx, summ)
            summ -= maaap[dy][dx]
            visited[dy][dx] = False


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    maap = []
    maaap = []
    visited = []
    for _ in range(N):
        temp = [int(char) for char in input()]
        maaap.append(temp)
        temp2 = [True] * N
        visited.append(temp2)
        temp3 = [[] for _ in range(N)]
        maap.append(temp3)
    maap[0][0] = 0
    for i in range(N-1):
        st = [(a, i) for a in range(i)]
        st += [(i, b) for b in range(i)]
        st.append((i, i))
        # print('st : ', st)
        for l in range(i+2):
            visited[i+1][l] = False
        for l in range(i+1):
            visited[l][i+1] = False
        # print('visited:')
        # for _ in range(N):
        #     for __ in range(N):
        #         print(visited[_][__], end=' ')
        #     print()
        #
        for sy, sx in st:
            go(sy, sx, maap[sy][sx])


        for _y in range(i+2):
            maap[_y][i+1] = min(maap[_y][i+1])
        for _x in range(i+1):
            maap[i+1][_x] = min(maap[i+1][_x])
        # print('maap :', maap)
        for l in range(i+2):
            visited[i+1][l] = True
        for l in range(i+1):
            visited[l][i+1] = True





    # print('after maap:')
    #
    # for _ in range(N):
    #     for __ in range(N):
    #         print(maap[_][__], end=' ')
    #     print()

    #go(0,0, 0)
    print('#{} {}'.format(tc, maap[N-1][N-1]))