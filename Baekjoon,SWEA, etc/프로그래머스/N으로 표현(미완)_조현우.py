def solution(N, number):
    a = [N, -N]
    b = []
    cnt = 1
    while True:
        if cnt > 8:
            return -1
        for item in a:
            b.append(item*10+N)
            b.append(item*10 - N)
            b.append(item + N)
            b.append(item - N)
            b.append(item * N)
            b.append(item * (-N))
            b.append(item // N)
            b.append(item - (N-1))
            b.append(item + (N-1))
            b.append(item + (N**2 - N))
            b.append(item - (N**2 - N))
        cnt += 1
        for item in b:
            if item == number:
                return cnt
        a = b.copy()
        b = []
    return answer
print(solution(2, 11))