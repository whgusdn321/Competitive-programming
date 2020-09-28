def solution(n, arr1, arr2):
    answer = []
    N = len(arr1)
    for i in range(N):
        a = [0] * N
        b = [0] * N
        num1 = arr1[i]
        num2 = arr2[i]
        for i in range(N - 1, 0, -1):
            a[i] = num1 % 2
            num1 //= 2
        a[0] = num1

        for i in range(N - 1, 0, -1):
            b[i] = num2 % 2
            num2 //= 2
        b[0] = num2
        c = [0] * N
        for i in range(N):
            c[i] = a[i] | b[i]
        temp = ""
        for item in c:
            if item == 1:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer


def solution(n, arr1, arr2):
    answer = []
    N = len(arr1)
    for i in range(N):
        a = arr1[i]
        a_temp = [0]*N
        j = N-1
        while j>=0 and a >= 0:
            k = a%2
            a //= 2
            a_temp[j] = k
            j -= 1
        b = arr2[i]
        b_temp = [0] * N
        j = N-1
        while j>=0 and b >= 0:
            k = b%2
            b //= 2
            b_temp[j] = k
            j -= 1
        ans = ''
        for i in range(N):
            if b_temp[i] | a_temp[i]:
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))