def make_combis(i, stakk1, stakk2):
    global combis, P, arr
    if i == P:
        combis.append((stakk1.copy(), stakk2.copy()))
        return
    stakk1.append(arr[i][0])
    make_combis(i+1, stakk1, stakk2)
    stakk1.pop()
    stakk2.append(arr[i][1])
    make_combis(i+1, stakk1, stakk2)
    stakk2.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(char) for char in input().split()]
        maap.append(temp)
    peoples = [None]
    stairs = []
    for i in range(N):
        for j in range(N):
            if maap[i][j] == 1:
                peoples.append((i, j))
            elif maap[i][j] != 0:
                stairs.append((i, j, maap[i][j]))
            else:
                pass
    P = len(peoples)
    arr = [[] for _ in range(P)]
    #print('peoples : ',peoples)
    for i in range(1, P):
        py, px = peoples[i][0], peoples[i][1]
        sy, sx = stairs[0][0], stairs[0][1]
        ssy, ssx = stairs[1][0], stairs[1][1]
        temp1 = abs(py-sy) + abs(px-sx)
        temp2 = abs(py-ssy) + abs(px-ssx)
        arr[i].append(temp1)
        arr[i].append(temp2)
    combis = []
    make_combis(1, [], [])
    results = []
    s1time = stairs[0][2]
    s2time = stairs[1][2]

    for combi in combis:
        q1 = combi[0]
        q1.sort()
        q2 = combi[1]
        q2.sort()
        stair1 = []
        stair2 = []
        time = 0
        while q1 or q2 or stair1 or stair2:
            while q1 and q1[0] < time and len(stair1) < 3:
                q1.pop(0)
                stair1.append(s1time)
            while q2 and q2[0] < time and len(stair2) < 3:
                q2.pop(0)
                stair2.append(s2time)
            for k in range(len(stair1)):
                stair1[k] -= 1
            for k in range(len(stair2)):
                stair2[k] -= 1
            next_stair1 = []
            next_stair2 = []
            for item in stair1:
                if item != 0:
                    next_stair1.append(item)
            for item in stair2:
                if item != 0:
                    next_stair2.append(item)
            stair1 = next_stair1
            stair2 = next_stair2
            time += 1
        results.append(time)
    print('#{} {}'.format(tc, min(results)))


