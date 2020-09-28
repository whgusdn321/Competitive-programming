def make_combis(i, stakk, limit):
    global N, combis
    if len(stakk) == limit:
        anothor = [i for i in range(N) if i not in stakk]
        combis.append([stakk.copy(), anothor])
        return
    for j in range(i+1, N):
        stakk.append(j)
        make_combis(j, stakk, limit)
        stakk.pop()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(char) for char in input().split()]
        maap.append(temp)
    limit = N // 2
    combis = []
    make_combis(-1, [], limit)
    #print('combis : ', combis)
    results = []
    for combi in combis:
        food1, food2 = combi
        a, b = 0, 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                a += maap[food1[i]][food1[j]]
                a += maap[food1[j]][food1[i]]
        for i in range(N//2):
            for j in range(i+1, N//2):
                b += maap[food2[i]][food2[j]]
                b += maap[food2[j]][food2[i]]
        results.append(abs(a - b))
    print('#{} {}'.format(tc, min(results)))




