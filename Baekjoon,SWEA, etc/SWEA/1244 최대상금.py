from copy import copy
T = int(input())
for tc in range(1, T+1):
    num, k = input().split(' ')
    num = [char for char in num]
    k = int(k)
    N = len(num)

    combis = []
    for i in range(N):
        for j in range(i+1, N):
            combis.append((i, j))

    queue = [num]
    for _ in range(k):
        next_queue = []
        for _num in queue:
            for combi in combis:
                new_num = copy(_num)
                a, b = combi
                temp = new_num[a]
                new_num[a] = new_num[b]
                new_num[b] = temp
                if new_num not in next_queue:
                    next_queue.append(new_num)
        queue = next_queue
        #print(_, 'queue : ', queue)
    numbers = []
    for num in queue:
        number = int(''.join(num))
        numbers.append(number)
    numbers.sort(reverse=True)
    print('#{} {}'.format(tc, numbers[0]))