def solution(K, travel):
    cur = [[travel[0][0], travel[0][1]], [travel[0][2], travel[0][3]]] #time, money
    N = len(travel)
    lefts = [0] * N
    sums = 0
    for i in range(N-1, -1, -1):
        sums += travel[i][2]
        lefts[i] = sums
    #print('lefts : ', lefts)
    max_money = max(travel[0][1], travel[0][3])
    for i in range(1, N):
        temp = []
        walk = [travel[i][0], travel[i][1]] #[800, 370]
        bycle = [travel[i][2], travel[i][3]]
        for j in range(len(cur)):
            time, money = cur[j]
            new_time1 = walk[0] + time
            new_money1 = walk[1] + money
            if i < N-1 and new_time1 + lefts[i+1] <= K:
                temp.append([new_time1, new_money1])
                if new_money1 > max_money:
                    max_money = new_money1
            elif new_time1  <= K:
                temp.append([new_time1, new_money1])
                if new_money1 > max_money:
                    max_money = new_money1


            new_time2 = bycle[0] + time
            new_money2 = bycle[1] + money
            if i < N-1 and new_time2 + lefts[i+1] <= K:
                temp.append([new_time2, new_money2])
                if new_money2 > max_money:
                    max_money = new_money2
            elif new_time2  <= K:
                temp.append([new_time2, new_money2])
                if new_money2 > max_money:
                    max_money = new_money2

        cur = temp
    return max_money





print(solution(1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]))
print(solution(3000, [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]))