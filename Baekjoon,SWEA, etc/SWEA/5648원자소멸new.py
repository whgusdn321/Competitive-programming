def move(electrons):
    global maap

    #상 : 0, 하: 1 좌: 2 우: 3
    for i in range(len(electrons)):
        #print('electrons[i', electrons[i])
        ey, ex, edir, ener = electrons[i]
        if edir == 0:
            if ey != 4000:
                #ener = maap[ey][ex]
                maap[ey][ex] -= ener
                ey += 1
                maap[ey][ex] += ener
                electrons[i][0] = ey
        elif edir == 1:
            if ey != 0:
                #ener = maap[ey][ex]
                maap[ey][ex] -= ener
                ey -= 1
                maap[ey][ex] += ener
                electrons[i][0] = ey
        elif edir == 2:
            if ex != 0:
                #ener = maap[ey][ex]
                maap[ey][ex] -= ener
                ex -= 1
                maap[ey][ex] += ener
                electrons[i][1] = ex
        else:
            if ex != 4000:
                #ener = maap[ey][ex]
                maap[ey][ex] -= ener
                ex += 1
                maap[ey][ex] += ener
                electrons[i][1] = ex


T = int(input())
maap = [[0 for _ in range(4001)] for __ in range(4001)]
for tc in range(1, T+1):
    electrons = []
    if tc != 1:
        for i in range(4001):
            maap[0][i] = 0
            maap[i][0] = 0
            maap[i][4000] = 0
            maap[4000][i] = 0

    N = int(input())
    for n in range(N):
        ex, ey, edir, eK = map(int, input().split())
        ey = (ey)*2 + 2000
        ex = (ex)*2 + 2000
        maap[ey][ex] = eK
        electrons.append([ey, ex, edir, eK])

    time = 0
    energys = 0

    while time < 4004 and electrons:
        move(electrons)  # update maap, electrons
        next_electrons = []
        for i in range(len(electrons)):
            ey, ex, _, eener = electrons[i]
            if maap[ey][ex] != eener:
                energys += maap[ey][ex]
                maap[ey][ex] = 0
            else:
                if ey == 0 or ey == 4000 or ex == 0 or ex == 4000:
                    maap[ey][ex] = 0
                else:
                    next_electrons.append(electrons[i])

        electrons = next_electrons
        time += 1
    print('#{} {}'.format(tc, energys))

