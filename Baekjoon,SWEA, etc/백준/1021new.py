import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


def leftmove(arr):
    a = arr.popleft()
    arr.append(a)


def rightmove(arr):
    a = arr.pop()
    arr.appendleft(a)


N, M = map(int, read().split())
elem = [int(a) for a in read().split()]
arr = [0] * N
for ele in elem:
    arr[ele-1] = ele
arr = deque(arr)

total = 0
for ele in elem:
    #print('ele : ', ele)
    i = 0
    j = len(arr) - 1

    left = 0
    right = 1
    while i < len(arr) and arr[i] != ele:
        i += 1
        left += 1

    while j >= 0 and arr[j] != ele:
        j -= 1
        right += 1

    if left <= right:
        total += left
        for _ in range(left):
            leftmove(arr)
        arr.popleft()
    else:
        total += right
        for _ in range(right):
            rightmove(arr)
        arr.popleft()
print(total)

'''
1021 구버젼. 교훈 : 전형적인 풀이 절차를 가지자..
일반적으로 회전하는 큐, 어레이가 나오면, deque를 사용해서..
pop(), appendleft()등을 사용해서 문제를 해결하는것이 일반적이다.
이것을 통째로 배열 인덱스간의 식을 만들어서 하면 머리터진다.
시험에서는 특히 쉽게 가야한다..
'''

import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()

N, M = map(int, read().split())
elem = [int(a) for a in read().split()]
arr = []
for ele in elem:
    left = ele - 1
    right = N - left
    arr.append([left, right])
queue = deque(arr)

print('queue : , ', queue)

cnt = 0
while queue:
    l, r = queue.popleft()
    N -= 1
    if l <= r:
        cnt += l
        for ele in queue:
            ele[0] = (ele[0] - l) % (N+1) -1
            ele[1] = ele[1] + l
    else:
        cnt += r
        for ele in queue:
            ele[0] = (ele[0] + r)%(N)
            ele[1] = N - ele[0]
    print('queue : ',queue)
print(cnt)
# for ele in elem:
#     arr[ele-1] = 1
# print('arr : ',arr)
#
#
# def left(n, arr):
#     temp = deque([0]*len(arr))
#     for i in range(len(arr)):
#         temp[i] = arr[(i+n)%len(arr)]
#     arr = temp.copy()
#     return arr
#
#
# def right(n, arr):
#     temp = deque([0]*len(arr))
#     for i in range(len(arr)):
#         temp[i] = arr[(i-n)%len(arr)]
#     arr = temp.copy()
#     return arr
#
#
# def measure(arr):
#     i, j = 0, 0
#     while arr[i] == 0:
#         i += 1
#     while arr[-j] == 0:
#         j += 1
#     return i, j
#
#
# cnt = 0
# k = 0
# while k<M:
#     k += 1
#     l, r = measure(arr)
#     if l <= r:
#         arr = left(l, arr)
#         cnt += l
#     else:
#         arr = right(r, arr)
#         cnt += r
#     print('k : {}, arr :{}'.format(k, arr))
#     arr.popleft()
#
# print('cnt : ',cnt)