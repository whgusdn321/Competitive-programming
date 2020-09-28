from copy import deepcopy
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    results = []
    arr= []

    for _ in range(N):
        temp = [int(a) for a in input().split()]
        arr.append(temp)
    temp = [[0] * N for _ in range(N)]
    for _ in range(3):
        for i in range(N):
            for j in range(N):
                temp[i][j] = arr[N-1-j][i]
        arr = deepcopy(temp)
        results.append(arr)
    print('#{}'.format(tc))
    for i in range(N):
        for arr in results:
            for item in arr[i]:
                print(item, end='')
            print(end=' ')
        print()