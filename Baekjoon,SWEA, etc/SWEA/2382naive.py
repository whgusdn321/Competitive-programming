def _move(maap1, maap2, y, x):
    if maap2[y][x][0] == 1:
        temp = maap1[y][x].pop(0)
        temp2 = maap2[y][x].pop(0)
        y -= 1
        maap1[y][x].append(temp)
        maap2[y][x].append(-temp2)
    elif maap2[y][x][0] == 2:
        temp = maap1[y][x].pop(0)
        temp2 = maap2[y][x].pop(0)
        y += 1
        maap1[y][x].append(temp)
        maap2[y][x].append(-temp2)
    elif maap2[y][x][0] == 3:
        temp = maap1[y][x].pop(0)
        temp2 = maap2[y][x].pop(0)
        x -= 1
        maap1[y][x].append(temp)
        maap2[y][x].append(-temp2)
    else:
        temp = maap1[y][x].pop(0)
        temp2 = maap2[y][x].pop(0)
        x += 1
        maap1[y][x].append(temp)
        maap2[y][x].append(-temp2)


def move(maap1, maap2):
    global N
    # 상 : 1, 하 : 2, 좌 : 3, 우 : 4
    for y in range(N):
        for x in range(N):
            if len(maap1[y][x]) >= 1 and maap2[y][x][0] > 0:
                """
                이 if 문이 중요한데, 한번 잘 생각해보자. maap1, maap2는 리스트이다.
                maap이 만약 list라면, 정말 세심한 주의를 기울여야 한다는 것을 인식하고 문제를 풀자..
                우선, 기본적으로 move할때 pop(0), append()를 쓸 것이다. 즉, FIFO형태가 되야함. 그래야 먼저 있던것이 제대로 옮겨진다.
                그다음, 또 주의해야 할것이 만약 len(maap1[y][x])처럼 리스트의 길이가 1이상인 곳이면 다 옮기는 방식은 역시 또 주의해야 하는데,
                만약 5x5의 맵에서 어떤부분(3,3)를 (3,4)로 옮겼다고 치자. 그러면 다음 for문을 실행할때, (3,4)를 한번 또 옮기는 상황이 발생한다.
                그래서 그것을 방지하기 위하여, 옮길때, 방향을 -1로 해주었다.
                그리고, maap1[y][x]가 1을 초과할때도 역시 옮겨줘야하는데, 그 이유는, 어떤것이 한곳에 모여도, 그 한곳에 모인곳에 아직 더 가야하는 놈이 있기 때문이다.
                그리고 그 가야하는 놈은 역시 제일 첫번째 위치에 있으므로 pop(0)를 해줘야한다.
                
                정리하자면,
                 1.list형태의 맵을 move 할때는 pop(0), append() 형식으로 move할것.
                 2.그리고 다양한 상황, 특히 한번 옮기고,그다음 loop명령을 실행할 때 또 중복되서 옮겨지지 않는가를 항상 염두하자.
                 
                 다음번에 문제를 풀 떄는 ,이러한 복잡성을 없애기 위해 next_maap 기법을 사용해보자.
                 
                
                """
                _move(maap1, maap2, y, x)


tcs = int(input())
for tc in range(1, tcs+1):
    N, time, K = map(int, input().split())
    germs = []
    maap1 = [[[] for _ in range(N)] for __ in range(N)]
    maap2 = [[[] for _ in range(N)] for __ in range(N)]
    for k in range(K):
        y, x, m, dirc = map(int, input().split())
        #germs.append([y, x, dirc, m])
        maap1[y][x].append(m)
        maap2[y][x].append(dirc)

    for _ in range(time):


        move(maap1, maap2)

        for i in range(N):
            for j in range(N):
                if maap2[i][j]:
                    for d in range(len(maap2[i][j])):
                        maap2[i][j][d] *= -1
        for x in range(N):
            if len(maap1[0][x]) == 1:
                maap1[0][x][0] //= 2
                maap2[0][x][0] = 2
        for x in range(N):
            if len(maap1[N-1][x]) == 1:
                maap1[N-1][x][0] //= 2
                maap2[N-1][x][0] = 1
        for y in range(N):
            if len(maap1[y][0]) == 1:
                maap1[y][0][0] //= 2
                maap2[y][0][0] = 4
        for y in range(N):
            if len(maap1[y][N-1]) == 1:
                maap1[y][N-1][0] //= 2
                maap2[y][N-1][0] = 3

        for i in range(1, N-1):
            for j in range(1, N-1):
                if len(maap1[i][j]) > 1:
                    maxidx = maap1[i][j].index(max(maap1[i][j]))
                    maap2[i][j] = [maap2[i][j][maxidx]]
                    maap1[i][j] = [sum(maap1[i][j])]
        # print('time : ',_)
        # print('maap1 : ')
        # for i in range(N):
        #     for j in range(N):
        #         print(maap1[i][j], end = '')
        #     print()
        #
        #
        # print('maap2 : ')
        # for i in range(N):
        #     for j in range(N):
        #         print(maap2[i][j], end='')
        #     print()


    ans = 0
    for i in range(N):
        for j in range(N):
            if len(maap1[i][j]) == 1:
                ans += maap1[i][j][0]
    print('#{} {}'.format(tc, ans))




