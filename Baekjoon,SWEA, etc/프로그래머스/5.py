def solution(stones, k):
    cnt = 0
    N = len(stones)
    while True:
        print('stones : ', stones)
        for i in range(N):
            if stones[i] != 0:
                stones[i] -= 1

        boool = True
        for i in range(N):
            if stones[i] == 0:
                boool = False
                for j in range(i, i + k):
                    if j >= N:
                        boool = True
                        break
                    if stones[j] > 0:
                        boool = True
                if boool == False:
                    break

        if boool:
            cnt += 1
        else:
            break

    return cnt

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))