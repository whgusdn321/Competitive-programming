def go(oper, before, i):
    global arr, N, results, opers
    if oper == '+':
        before += arr[i]
    elif oper == '*':
        before *= arr[i]
    elif oper == '/':
        if before < 0 and arr[i] > 0:
            before *= -1
            before //= arr[i]
            before *= -1
        else:
            before //=arr[i]
    else:
        before -= arr[i]

    if i == N-1:
        results.append(before)
        return

    if opers[0] > 0:
        opers[0] -= 1
        go('+', before, i+1)
        opers[0] += 1
    if opers[1] > 0:
        opers[1] -= 1
        go('-', before, i+1)
        opers[1] += 1
    if opers[2] > 0:
        opers[2] -= 1
        go('*', before, i+1)
        opers[2] += 1
    if opers[3] > 0:
        opers[3] -= 1
        go('/', before, i+1)
        opers[3] += 1

def go2(before, i):
    global arr, N, results, opers
    if i == N:
        results.append(before)
        return
    else:
        if opers[0] > 0:
            opers[0] -= 1
            go2(before + arr[i], i + 1)
            opers[0] += 1
        if opers[1] > 0:
            opers[1] -= 1
            go2(before - arr[i], i + 1)
            opers[1] += 1
        if opers[2] > 0:
            opers[2] -= 1
            go2(before * arr[i], i + 1)
            opers[2] += 1
        if opers[3] > 0:
            opers[3] -= 1
            if before < 0 and arr[i] > 0:
                go2(-((-before)//arr[i]), i + 1)
            else:
                go2(before//arr[i], i+1)
            opers[3] += 1


N = int(input())
arr = [int(char) for char in input().split()]
opers = [int(char) for char in input().split()]
results = []
go2(arr[0], 1)
print(max(results))
print(min(results))