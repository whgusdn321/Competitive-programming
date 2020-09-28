def solution(weight):
    weight.sort()

    if 1 not in weight:
        return 1
    else:
        a = 0
        for i in range(len(weight)):
            if weight[i] - 1 <= a:
                a += weight[i]
            else:
                break
        return a + 1