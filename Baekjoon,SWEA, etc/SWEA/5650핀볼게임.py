"""
알고리즘 자체는 전형적인, 시뮬래이션 문제이다.(방향을 가진 공과, 공이 옮겨 다니면서 조건에 따라 방향이 변하는 문제 임)
간단하다고 느꼈지만 2가지 실수를 하여 시간이 많이 늦어졌다.

이 문제를 풀며 2가지 실수를 하였다. 첫번째, go 함수안에 일딴 가고나서 검사하는 알고리즘..에서
가고나서 검사할때 범위가 벗어날 수 있는 경우가 생긴다는 것을 캐치 못하였음. 나중에 한번 더 풀때, 가고나서 검사하기 직전 어떤 경우들이 있는가 곰곰히 생각해보고 코드짜보자. ->모든 경우의 수 채크 실수

두번째. 두번째 실수만 아니였으면 최소한 2시간 안에 풀었을 것이다. 두번째 실수는 무엇을 했냐면, 벽에 부딫혔을때, 다음 공의 포지션이 어떻게 되는가를 착각했다.
나는 공이 벽에 부딫히는 조건을 공이 범위가 벗어나면 범위가 벗어나는 조건에 걸려 벽에 맞았다고 했다. 그래서 공의 범위가 벗어나면, 방향 반대로 해주고,
반대방향으로 한칸 가서 복귀시키는 알고리즘을 생각해냈지만, 오류가 있었다. 벽 바로 곁에 아무런 블록(삼각형 or 사각형)이 없으면 이렇게 해도 된다..하지만,
곁에 블록이 있다면, 블록을 한칸 무시하고 뛰어 넘을 수 있다.  이러한 오류는 진짜 그러한 상황이 떠올라 먼져 캐치가 되면 좋겠지만 현실적으로 그럴 가능성은 적다.
그냥 시뮬래이션을 조금 머릿속으로 해보는 수 밖에 없다.

"""


def move(ball):
    dirc = ball['dir']
    if dirc == 'E':
        ball['x'] += 1
    elif dirc == 'W':
        ball['x'] -= 1
    elif dirc == 'S':
        ball['y'] += 1
    else:
        ball['y'] -= 1


def adjust(ball, maap, cnt):
    global womholes
    y, x, dirc = ball['y'], ball['x'], ball['dir']
    #Wall
    if not(0<=y<N and 0<=x<N):
        if dirc == 'E':
            dirc = 'W'
            #x -= 1
        elif dirc == 'W':
            dirc = 'E'
            #x += 1
        elif dirc == 'S':
            dirc = 'N'
            #y -= 1
        else:
            dirc = 'S'
            #y += 1
        ball['y'], ball['x'], ball['dir'] = y, x, dirc
        cnt +=1
        return cnt

    # 삼각형
    if maap[y][x] == 1:
        if dirc == 'E':
            dirc = 'W'
        elif dirc == 'N':
            dirc = 'S'
        elif dirc == 'W':
            dirc = 'N'
        else:
            dirc = 'E'
        cnt += 1
    elif maap[y][x] == 2:
        if dirc == 'E':
            dirc = 'W'
        elif dirc == 'N':
            dirc = 'E'
        elif dirc == 'W':
            dirc = 'S'
        else:
            dirc = 'N'
        cnt += 1
    elif maap[y][x] == 3:
        if dirc == 'E':
            dirc = 'S'
        elif dirc == 'N':
            dirc = 'W'
        elif dirc == 'W':
            dirc = 'E'
        else:
            dirc = 'N'
        cnt += 1
    elif maap[y][x] == 4:
        if dirc == 'E':
            dirc = 'N'
        elif dirc == 'N':
            dirc = 'S'
        elif dirc == 'W':
            dirc = 'E'
        else:
            dirc = 'W'
        cnt += 1
    elif maap[y][x] == 5:
        if dirc == 'E':
            dirc = 'W'
        elif dirc == 'N':
            dirc = 'S'
        elif dirc == 'W':
            dirc = 'E'
        else:
            dirc = 'N'
        cnt += 1
    else:
        y, x = womholes[(y, x)]
    ball['y'], ball['x'], ball['dir'] = y, x, dirc
    return cnt


def go(ball):
    cnt = 0
    sy, sx = ball['y'], ball['x']
    while True:
        move(ball)
        if 0 <= ball['y'] < N and 0 <= ball['x'] < N:
            if (ball['y'], ball['x']) == (sy, sx) or maap[ball['y']][ball['x']] == -1:
                return cnt
        if 0 <= ball['y'] < N and 0 <= ball['x'] < N and maap[ball['y']][ball['x']] == 0:
            continue
        else:
            cnt = adjust(ball, maap, cnt)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(a) for a in input().split()]
        maap.append(temp)
    results = []
    womholes = {}
    for i in range(N):
        for j in range(N):
            if 6 <= maap[i][j] < 11:
                boool = True
                for key, item in womholes.items():
                    if item == maap[i][j]:
                        womholes[(i, j)] = key
                        womholes[key] = (i, j)
                        boool = False
                        break
                if boool:
                    womholes[(i, j)] = maap[i][j]
    for i in range(N):
        for j in range(N):
            if maap[i][j] == 0:
                for dirc in ['E', 'W', 'N', 'S']:
                    ball = {'y':i, 'x':j, 'dir': dirc}
                    cnt = go(ball)
                    results.append(cnt)
    print('#{} {}'.format(tc, max(results)))
