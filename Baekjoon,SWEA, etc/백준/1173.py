N, m, M, T, R = map(int, input().split())

if m + T > M: #운동을 끝낼 수 없는경우 :
    print(-1)
else:
    cur_m = m #현재 맥박
    n = 0 # 운동한시간
    nn = 0 #운동 + 휴식 시간
    while True:
        if n == N:
            break
        if cur_m + T <= M:
            n += 1
            nn += 1
            cur_m += T
        else:
            while cur_m + T > M:
                cur_m -= R
                nn += 1
                if cur_m < m:
                    cur_m = m
    print(nn)