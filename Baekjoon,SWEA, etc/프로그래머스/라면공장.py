def solution(stock, dates, supplies, k):
    cnt = 0
    N = len(dates)
    dates.append(k)
    stock -= dates[0]
    for i in range(N):
        if i > 0:
            stock -= (dates[i] - dates[i - 1])
        tempstock = stock
        for j in range(i + 1, len(dates)):
            if tempstock < dates[j] - dates[i]:
                stock += supplies[i]
                print('stock : ', stock)
                cnt += 1
                break
            else:
                if j < N:
                    tempstock += supplies[j]

    return cnt
