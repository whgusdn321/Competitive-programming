read = lambda :input()
test_cases = int(input())
maap = [[0 for _ in range(4001)] for __ in range(4001)]


def move(electrons):
    global maap
    for electron in electrons:
        x, y, dir, ener = electron
        if dir == 0: #상
            maap[y][x] -= ener
            y += 1
            if y <= 4000:
                maap[y][x] += ener
            electron[1] = y
        elif dir == 1: # 하
            maap[y][x] -= ener
            y -= 1
            if y >= 0:
                maap[y][x] += ener
            electron[1] = y
        elif dir == 2: # 좌
            maap[y][x] -= ener
            x -= 1
            if x >= 0:
                maap[y][x] += ener
            electron[0] = x
        else:
            maap[y][x] -= ener
            x += 1
            if x <= 4000:
                maap[y][x] += ener
            electron[0] = x


for test_case in range(1, test_cases+1):
    N = int(input())

    for i in range(4001):
        maap[0][i] = 0
        maap[i][0] = 0
        maap[i][4000] = 0
        maap[4000][i] = 0

    electrons = []
    for _ in range(N):
        x, y, dir, ener = map(int, read().split())
        x = x*2 + 2000
        y = y*2 + 2000
        electrons.append([x, y, dir, ener])
        maap[y][x] = ener

    energy_sum = 0

    for _ in range(4004):

        move(electrons)  # 0.5초씩 이동
        next_electron = []
        to_terminate = []

        for i in range(len(electrons)): # electrons를 한번 돌면서..  이시간대에 서로 만난놈들은 전부 없애주고, 끝에 모서리에 닿은놈 또한 없애준다.
            x, y, __, ener = electrons[i]
            if y == -1 or y == 4001 or x == -1 or x == 4001:
                to_terminate.append(i)
            elif maap[y][x] != ener:
                to_terminate.append(i)
                energy_sum += ener

        for i in range(len(electrons)):
            if i not in to_terminate:
                next_electron.append(electrons[i])
            else:
                x, y, __, ener = electrons[i]
                if 0<=y<4001 and 0<=x<4001:
                    maap[y][x] -= ener
        electrons = next_electron

    print('#{} {}'.format(test_case, energy_sum))









