testcases = 10
for testcase in range(1, testcases+1):
    _ = input()
    arr = []
    for _ in range(100):
        temp = [int(a) for a in input().split()]
        arr.append(temp)

    sums = []
    #행
    for i in range(100):
        sums.append(sum(arr[i]))
    #열
    for j in range(100):
        summ = 0
        for i in range(100):
            summ += arr[i][j]
        sums.append(summ)

    # #대각1
    # for i in range(1, 100):
    #     cur = [i, 0]
    #     dy, dx = (1, 1)
    #     summ = arr[cur[0]][cur[1]]
    #     while (cur[0] + dy) < 100 and (cur[1] + dx)<100:
    #         cur[0] += dy
    #         cur[1] += dx
    #         summ += arr[cur[0]][cur[1]]
    #     sums.append(summ)
    # #대각2
    # for j in range(0, 100):
    #     cur = [0, j]
    #     dy, dx = (1, 1)
    #     summ = arr[cur[0]][cur[1]]
    #     while (cur[0] + dy) < 100 and (cur[1] + dx) < 100:
    #         cur[0] += dy
    #         cur[1] += dx
    #         summ += arr[cur[0]][cur[1]]
    #     sums.append(summ)
    # #대각3
    # for j in range(0, 100):
    #     cur = [0, j]
    #     dy, dx = (1, -1)
    #     summ = arr[cur[0]][cur[1]]
    #     while (cur[0] + dy) < 100 and (cur[1] + dx) < 100:
    #         cur[0] += dy
    #         cur[1] += dx
    #         summ += arr[cur[0]][cur[1]]
    #     sums.append(summ)
    # #대각4
    # for i in range(1, 100):
    #     cur = [i, 99]
    #     dy, dx = (1, -1)
    #     summ = arr[cur[0]][cur[1]]
    #     while (cur[0] + dy) < 100 and (cur[1] + dx) < 100:
    #         cur[0] += dy
    #         cur[1] += dx
    #         summ += arr[cur[0]][cur[1]]
    #     sums.append(summ)

    #대각 1
    summ =0
    for i in range(0, 100):
        summ += arr[i][i]
    sums.append(summ)
    #대각 2
    summ =0
    for i in range(i,100):
        summ += arr[i][99-i]
    sums.append(summ)
    print("#{} {}".format(testcase, max(sums)))

