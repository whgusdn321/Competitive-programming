#import sys
#sys.stdin = open("sample_input.txt", "r")
read = lambda :input()
from collections import deque

test_cases = int(read())

for test_case in range(1, test_cases+1):
    N ,K = map(int, read().split())
    sutza = [a for a in read()]
    for i in range(len(sutza)) :
        if sutza[i] == 'A':
            sutza[i] = 10
        elif sutza[i] == 'B':
            sutza[i] = 11
        elif sutza[i] == 'C':
            sutza[i] = 12
        elif sutza[i] == 'D':
            sutza[i] = 13
        elif sutza[i] == 'E':
            sutza[i] = 14
        elif sutza[i] == 'F':
            sutza[i] = 15
        else:
            sutza[i] = int(sutza[i])

    numbers = []
    queue = deque(sutza)

    # without rotation
    for i in range(0, len(queue), N//4):
        k = N // 4 - 1
        sum = 0
        for j in range(i, i+N//4):
            sum += (16**k) * queue[j]
            k -= 1
        if sum not in numbers:
            numbers.append(sum)

    # with rotation :
    for _ in range(N//4-1):
        a = queue.pop()
        queue.appendleft(a)
        for i in range(0, len(queue), N // 4):
            k = N // 4 - 1
            sum = 0
            for j in range(i, i + N // 4):
                sum += (16 ** k) * queue[j]
                k -= 1
            if sum not in numbers:
                numbers.append(sum)
    numbers.sort(reverse=True)
    ans = numbers[K-1]
    print('#{} {}'.format(test_case, ans))
