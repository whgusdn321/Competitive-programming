from collections import deque

T = int(input())
for tc in range(1, T+1):
    N , K = map(int, input().split())
    string = [char for char in input()]
    queue = deque(string)
    sett = set([])

    for i in range(0, N, N//4):
        num = ''
        for j in range(i, i+N//4):
            num += queue[j]
        real_num = int('0x'+num, 0)
        sett.add(real_num)
    for _ in range(N//4-1):
        t = queue.pop()
        queue.appendleft(t)
        for i in range(0, N, N // 4):
            num = ''
            for j in range(i, i + N // 4):
                num += queue[j]
            real_num = int('0x' + num, 0)
            sett.add(real_num)
    #print('sett : ', sett)

    arr = sorted(sett, reverse=True)
    print('#{} {}'.format(tc, arr[K-1]))


