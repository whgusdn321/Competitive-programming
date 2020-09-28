def changenum(num, stack):
    i = stack[0]
    j = stack[1]
    temp = num[i]
    num[i] = num[j]
    num[j] = temp

    return num


def go(d, k, before, stackk, num):
    global N, L, result, visited
    if d == 2*L + 1:
        if result < int(''.join(num)):
            result = int(''.join(num))
        return

    if  k == 0 and int(''.join(num)) in visited[d]:
        return

    visited[d].append(int(''.join(num))) # k == 0 일때나 k == 1일때나 상관없다.

    if k == 0:
        for i in range(N):
            stackk.append(i)
            go(d+1, (k+1)%2, i, stackk, num)
            stackk.pop()

    else: ## k == 1:
        for i in range(N):
            if i != before:
                stackk.append(i)
                go(d+1, (k+1)%2, i, [], changenum(num.copy(), stackk))
                stackk.pop()



testcases = int(input())
for testcase in range(1, testcases + 1):
    num, L = input().split()
    L = int(L)
    num = [char for char in num]
    N = len(num)
    result = 0

    visited = [[] for _ in range(2*L + 1)]
    go(0, 0, None, [], num)
    print('#{} {}'.format(testcase, result))