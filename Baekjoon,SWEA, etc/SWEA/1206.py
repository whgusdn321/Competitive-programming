for testcase in range(1, 11):
    n = int(input())
    arr =  [int(a) for a in input().split()]
    cnts = 0
    for i in range(2, n-2):
        value = arr[i]
        cnt = 0
        while value > arr[i-1] and value > arr[i-2] \
            and value > arr[i+1] and value > arr[i+2]:
            cnt += 1
            value -= 1
        cnts += cnt
    print('#{} {}'.format(testcase, cnts))


