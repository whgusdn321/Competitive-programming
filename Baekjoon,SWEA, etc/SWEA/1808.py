from collections import deque
# def go(mode, n, cnt):
#     global availables, wanted, results, visited
#     print('mode : ', mode)
#     print('n :', n)
#     print('cnt : ', cnt)
#     print('wanted :', wanted)
#     print()
#     if n > wanted:
#         return
#     elif n == wanted:
#         if visited[wanted] == -1 or cnt < visited[wanted]:
#             visited[wanted] = cnt
#         return
#     elif mode == 'mul':
#         for a in availables:
#             go('normal', n*a, cnt+1)
#
#     else:  # mode == 'normal'
#         # if visited[n] != -1 and cnt > visited[n]+1:
#         #     return
#         # else:  # visited[n] == -1 or cnt < visited[n]
#         visited[n] = cnt
#         for a in availables:
#             go('normal', n*10 + a, cnt+1)
#         go('mul', n, cnt+1)
#
#
#
#
#


T = int(input())
for tc in range(1, T+1):
    temp = [int(char) for char in input().split()]
    availables = [i for i in range(10) if temp[i]]
    queue = deque([(item, 1, 'normal') for item in availables])

    wanted = int(input())
    if wanted < 10:
        visited = [0] *10
    else:
        visited = [0] * (wanted+1)

    for a in availables:
        visited[a] = 1
    result = 0

    while queue:
        n, cnt, mode = queue.popleft()
        #print('n : {}, cnt : {}, mode : {}'.format(n, cnt, mode))
        if n == wanted:
            result = cnt
            break
        if mode == 'normal':
            for a in availables:
                next_n = n*10 + a
                next_cnt = cnt + 1
                if next_n <= wanted and visited[next_n] < 2:
                    visited[next_n] += 1
                    queue.append((next_n, next_cnt, 'normal'))
            if visited[n] < 2:
                visited[n] += 1
                queue.append((n, cnt+1, 'mul'))
        else: # mul
            for a in availables:
                next_n = n*a
                next_cnt = cnt + 1
                if next_n <= wanted and visited[next_n] < 2:
                    visited[next_n] += 1
                    queue.append((next_n, next_cnt, 'normal'))


    if result == 0:
        print('#{} {}'.format(tc,-1))
    else:
        print('#{} {}'.format(tc, result+1))
    #print(visited[wanted]+1)

