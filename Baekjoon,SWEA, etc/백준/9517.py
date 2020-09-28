from collections import deque
k = int(input())
n = int(input())
questions = []
for _ in range(n):
    a, b = input().split()
    questions.append([int(a), b])

queue = deque(questions)
arr = [0]*8
i = k-1
while 1:
    sum_temp = 0
    while queue:
        a, oper = queue.popleft()
        sum_temp += a
        if oper != 'T':
            continue
        else:
            break
    if not queue:
        print(i+1)
        break
    arr[i] = arr[(i-1)%8] + sum_temp
    if arr[i] >= 210:
        print(i+1)
        break
    i = (i+1)%8