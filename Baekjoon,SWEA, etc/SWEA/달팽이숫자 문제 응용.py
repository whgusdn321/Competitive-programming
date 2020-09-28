"""
안에서 부터 바깥쪽으로 나가는 달팽이 숫자 만들기
Ex : N == 4이면,

10 9 8 7  19
11 2 1 6  18
12 3 4 5 17
13 14 15 16
이렇게 되게 출력하라!
"""

print('# N 을 입력하세요 :')
N = int(input())

arr = [[0] * N for _ in range(N)]

if N %2 == 0: #N 이 짝수일때:
    sy, sx = N//2-1, N//2
    sn = 1
    for k in range(2, N+1, 2):
        l = k-1
        for i in range(0, l-1):
            arr[sy][sx] = sn
            sn += 1
            sy, sx = sy-1, sx
        for i in range(0, l):
            arr[sy][sx] = sn
            sn += 1
            sy, sx = sy, sx-1
        for i in range(0, l):
            arr[sy][sx] = sn
            sn += 1
            sy, sx = sy + 1, sx
        for i in range(0, l+1):
            arr[sy][sx] = sn
            sn += 1
            sy, sx = sy, sx + 1
else:
    sy, sx = N //2, N //2
    sn = 1
    for k in range(1, N + 1, 2):
        l = k - 1
        for i in range(0, l - 1):
            arr[sy][sx] = sn
            sn += 1
            sy, sx = sy - 1, sx
        for i in range(0, l):
            arr[sy][sx] = sn
            sn += 1
            sy, sx = sy, sx - 1
        for i in range(0, l):
            arr[sy][sx] = sn
            sn += 1
            sy, sx = sy + 1, sx
        for i in range(0, l + 1):
            arr[sy][sx] = sn
            sn += 1
            sy, sx = sy, sx + 1

print('arr : ')
for i in range(N):
    for j in range(N):
        print('{0:4d}'.format(arr[i][j]), end=' ')
    print()


