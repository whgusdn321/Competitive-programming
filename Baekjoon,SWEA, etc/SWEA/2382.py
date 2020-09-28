def move(germs, maap):
    # 상 = 1 하 = 2 좌 = 3 우 = 4
    """
    :param germs:
    :param maap:
    :return: changed germs and maap
    """
    for germ in germs:
        y, x, dirc, m = germ
        if dirc == 1:
            idx = maap[y][x].pop()
            y -= 1
            maap[y][x].insert(0, idx)
            germ[0] = y
        elif dirc == 2:
            idx = maap[y][x].pop()
            y += 1
            maap[y][x].insert(0, idx)
            germ[0] = y
        elif dirc == 3:
            idx = maap[y][x].pop()
            x -= 1
            maap[y][x].insert(0, idx)
            germ[1] = x
        else:#우
            idx = maap[y][x].pop()
            x += 1
            maap[y][x].insert(0, idx)
            germ[1] = x



tcs = int(input())
for tc in range(1, tcs+1):
    N, time, K = map(int, input().split())
    germs = []
    maap = [[[] for _ in range(N)] for __ in range(N)]
    for k in range(K):
        y, x, m, dirc = map(int, input().split())
        germs.append([y, x, dirc, m])
        maap[y][x].append(k)

    for _ in range(time):
        next_germs = []
        visited = []

        move(germs, maap)
        cnt = 0
        for i, germ in enumerate(germs):
            if i in visited:
                continue
            _y, _x, _dirc, _m = germ

            if _y == 0 or _y == N-1 or _x == 0 or _x == N-1:
                _m //= 2
                if _dirc == 1:
                    _dirc = 2
                elif _dirc == 2:
                    _dirc = 1
                elif _dirc == 3:
                    _dirc = 4
                else:
                    _dirc = 3
                next_germs.append([_y, _x, _dirc, _m])
                maap[_y][_x]= [cnt]
            elif len(maap[_y][_x]) != 1:
                _germs = [germs[j] for j in maap[_y][_x]]
                new_dirc = 0
                new_m = 0
                _germs.sort(key=lambda x:x[3], reverse=True)
                summ = 0
                for __,__,__,m in _germs:
                    summ += m
                new_m = summ
                new_dirc = _germs[0][2]
                next_germs.append([_y, _x, new_dirc, new_m])
                for j in maap[_y][_x]:
                    visited.append(j)
                maap[_y][_x] = [cnt]

            else:
                next_germs.append([_y, _x, _dirc, _m])
                maap[_y][_x] = [cnt]
            cnt += 1
        germs = next_germs

    result = 0
    for _, _, _, m in germs:
        result += m
    print('#{} {}'.format(tc, result))








